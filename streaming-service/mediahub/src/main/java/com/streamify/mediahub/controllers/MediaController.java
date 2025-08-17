package com.streamify.mediahub.controllers;

import com.streamify.mediahub.dto.BodyFilesDTO;
import com.streamify.mediahub.dto.ResponseErrorDTO;
import com.streamify.mediahub.services.MediaService;
import com.streamify.mediahub.services.RedisService;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.UrlResource;
import org.springframework.core.io.support.ResourceRegion;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import java.io.IOException;
import java.util.Map;


@RestController
@RequestMapping("/media")
public class MediaController {

    @Value("${flask.server}")
    private String flaskUrl;

    private final MediaService mediaService;
    private final RedisService redisService;

    public MediaController(MediaService mediaService, RedisService redisService) {
        this.mediaService = mediaService;
        this.redisService = redisService;
    }

    @PostMapping(path = "/upload")
    public void uploadMedia(HttpServletRequest request) {
        Map<String, String[]> metadata = request.getParameterMap();

        try{
            Map<String, Object> body = mediaService.writeMedia(request.getParts());

            for (String key : metadata.keySet()) {
                String[] value = metadata.get(key);
                    
                if (mediaService.hasUUID(value)) {
                    body.put(key, value);
                } else {
                    body.put(key, value[0]);
                }
            }
            redisService.push("spring:content:upload:success", body);

        } catch (Exception ex) {
            redisService.push("spring:content:upload:error", ex.getMessage());
        }
    }

    @GetMapping("/thumbnails/{thumbnailFile}")
    public ResponseEntity<?> getThumbnails(@PathVariable String thumbnailFile) {
        try {
            UrlResource thumbnailData = mediaService.getThumbnail(thumbnailFile);
            return ResponseEntity
                    .ok()
                    .contentType(MediaType.IMAGE_JPEG)
                    .body(thumbnailData);
        } catch (RuntimeException e) {
            ResponseErrorDTO responseError = new ResponseErrorDTO(
                    "Error",
                    "An error occurred while displaying the thumbnail",
                    Map.of("details", e.getMessage()));
            return ResponseEntity
                    .status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(responseError);
        }
    }

    @GetMapping(value = "/streaming/{fileName}/")
    public ResponseEntity<ResourceRegion> contentStream(
            @PathVariable String fileName,
            @RequestParam String source,
            @RequestHeader HttpHeaders headers
    ) {
        FileSystemResource video = mediaService.getResource(fileName, source);
        HttpRange range = headers.getRange().isEmpty() ? null : headers.getRange().get(0);

        try {
            long contentLength = video.contentLength();
            ResourceRegion region;

            if (range == null) {
                long chunkSize = Math.min(1_000_000, contentLength);
                region = new ResourceRegion(video, 0, chunkSize);
            } else {
                long start = range.getRangeStart(contentLength);
                long end = range.getRangeEnd(contentLength);
                long rangeLength = Math.min(1_000_000, end - start + 1);
                region = new ResourceRegion(video, start, rangeLength);
            }

            return ResponseEntity
                    .status(HttpStatus.PARTIAL_CONTENT)
                    .contentType(MediaTypeFactory.getMediaType(video)
                            .orElse(MediaType.APPLICATION_OCTET_STREAM))
                    .body(region);
        } catch (IOException e) {
            return null;
        }
    }

    @ResponseBody
    @DeleteMapping("/")
    public ResponseEntity<?> deleteMedia(@RequestBody BodyFilesDTO request) {
        try {
            mediaService.deleteMedia(
                    request.thumbnailFile(),
                    request.contentFile(),
                    request.trailerFile()
            );
            return ResponseEntity
                    .ok()
                    .build();
        } catch (RuntimeException e) {
            ResponseErrorDTO responseException = new ResponseErrorDTO(
                    "Error",
                    "An error occurred while deleting media",
                    Map.of("details", e.getMessage()));
            return ResponseEntity
                    .status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(responseException);
        }
    }
}
