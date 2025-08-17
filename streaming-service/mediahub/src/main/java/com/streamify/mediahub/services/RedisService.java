package com.streamify.mediahub.services;

import com.google.gson.Gson;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import redis.clients.jedis.Jedis;
import java.util.Map;

@Service
public class RedisService {

    @Value("${redis.host}")
    private String host;

    @Value("${redis.port}")
    private int port;

    private Jedis jedis;
    private Gson gson;

    public RedisService() {}

    @PostConstruct
    public void init() {
        this.jedis = new Jedis(host, port);
        this.gson = new Gson();
    }
    
    public void push(String key, Map<String, Object> value) {
        jedis.rpush(key, gson.toJson(value));
    }

    public void push(String key, String value) {
        jedis.rpush(key, value);
    }
}
