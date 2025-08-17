package com.streamify.mediahub.dto;

public record BodyFilesDTO(
        String thumbnailFile,
        String contentFile,
        String trailerFile
) {}
