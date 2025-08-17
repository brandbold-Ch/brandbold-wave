package com.streamify.mediahub.services;

import redis.clients.jedis.Jedis;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.springframework.stereotype.Service;
import com.google.gson.Gson;
import com.streamify.mediahub.dto.BodyFilesDTO;


@Service
public class RedisWorkerService {
    
    private final Jedis jedis;
    private final Gson gson;
    private final MediaService mediaService;
    private final ExecutorService executorService = Executors.newSingleThreadExecutor();

    public RedisWorkerService(Jedis jedis, MediaService mediaService) {
        this.jedis = jedis;
        this.mediaService = mediaService;
        this.gson = new Gson();

        processEvent();
    }

    private void processEvent() {
        executorService.submit(() -> {
            System.out.println("🎧 Listening to Redis in spring server...");

            while (true) {
                try {
                    List<String> events = jedis.blpop(0, "flask:metadata:save:rollback");

                    if (events != null) {                       
                        mediaService.deleteMedia(
                            gson.fromJson(events.get(1), BodyFilesDTO.class)
                        );
                        System.out.println("<Several contents were removed due to an error>");
                    }
                } catch (Exception ex) {
                    System.out.println("<Critical error during processing>: " + ex.getMessage());
                    Thread.sleep(1000);
                }
            }
        });
    }
}
