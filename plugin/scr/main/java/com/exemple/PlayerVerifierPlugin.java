package com.example;

import okhttp3.*;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;
import java.io.IOException;

public class PlayerVerifierPlugin extends JavaPlugin implements Listener {
    private final OkHttpClient httpClient = new OkHttpClient();

    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
        getLogger().info("PlayerVerifierPlugin включён!");
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        String playerName = event.getPlayer().getName();
        String apiUrl = "СВОЙ СЕРВЕР" + playerName;

        Request request = new Request.Builder()
                .url(apiUrl)
                .build();

        httpClient.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                getLogger().warning("Ошибка API: " + e.getMessage());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) {
                    getLogger().warning("API error: " + response.code());
                    return;
                }

                String json = response.body().string();
                boolean isVerified = json.contains("\"verified\":true");

                if (!isVerified) {
                    getServer().getScheduler().runTask(PlayerVerifierPlugin.this, () -> {
                        event.getPlayer().kickPlayer("🔒 Пройдите верификацию на сайте!");
                    });
                }
            }
        });
    }
}
