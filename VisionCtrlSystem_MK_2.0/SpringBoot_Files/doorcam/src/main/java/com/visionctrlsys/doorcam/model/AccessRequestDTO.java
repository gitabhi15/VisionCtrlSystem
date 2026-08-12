package com.visionctrlsys.doorcam.model;

public class AccessRequestDTO {
    private String username, action, cam_id, timestamp;

    public AccessRequestDTO() {

    }

    public AccessRequestDTO(String username, String action, String cam_id, String timestamp) {
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

}
