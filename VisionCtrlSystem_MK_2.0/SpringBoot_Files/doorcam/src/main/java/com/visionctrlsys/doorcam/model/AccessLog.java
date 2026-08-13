package com.visionctrlsys.doorcam.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "access_logs")
public class AccessLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username, timestamp, cam_id, action;

    public AccessLog() {
    }

    public AccessLog(String username, String action, String cam_id, String timestamp) {
        this.username = username;
        this.action = action;
        this.cam_id = cam_id;
        this.timestamp = timestamp;
    }

    public String getUsername() {
        return username;
    }

    public String getAction() {
        return action;
    }

    public String getCam_id() {
        return cam_id;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public Long getId() {
        return id;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public void setCam_id(String cam_id) {
        this.cam_id = cam_id;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public void setId(Long id) {
        this.id = id;
    }
}
