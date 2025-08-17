package com.streamify.mediahub.config;

import redis.clients.jedis.Jedis;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;


@Configuration
public class RedisWorkerConfig {
    
    @Value("${redis.host}")
    private String host;

    @Value("${redis.port}")
    private int port;

    @Bean
    public Jedis jedisClient() {
        return new Jedis(host, port);
    }
}
