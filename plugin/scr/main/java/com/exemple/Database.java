package com.example;

import java.sql.*;

public class Database {
    private Connection connection;

    public Database() {
        connect();
    }

    private void connect() {
        try {
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite:plugins/TelegramAuth/users.db");
            createTables();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void createTables() {
        try (Statement stmt = connection.createStatement()) {
            stmt.execute("CREATE TABLE IF NOT EXISTS users (" +
                    "telegram_id INTEGER PRIMARY KEY, " +
                    "mc_username TEXT NOT NULL)");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
