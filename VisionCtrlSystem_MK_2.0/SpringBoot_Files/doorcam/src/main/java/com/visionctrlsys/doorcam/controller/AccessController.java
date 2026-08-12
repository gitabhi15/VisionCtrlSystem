package com.visionctrlsys.doorcam.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.visionctrlsys.doorcam.model.AccessRequestDTO;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/api/v1")
public class AccessController {
    @PostMapping("/access")
    public String httpResponse(@RequestBody AccessRequestDTO jsonObject) {

        final String successMessage = "Data received successfully!";
        final String failureMessage = "Data wasn't received as expected. Please try again.";
        final String heartbeatMessage = "Status ok. No distinct faces detected in frame of focus.";
        String username = null;
        String timestamp = null;
        int successCounter = 0;

        String cam_id = jsonObject.getCam_id();
        if (cam_id != null)
            successCounter++;

        String action = jsonObject.getAction();
        if (action != null) {
            successCounter++;
            if (action.equals("STATUS_OK")) {
                System.out.println(heartbeatMessage);
            } else if (action.equals("ACCESS_REQUEST") || action.equals("UNKNOWN_FACE")) {
                username = jsonObject.getUsername();
                if (username != null)
                    successCounter++;

                timestamp = jsonObject.getTimestamp();
                if (timestamp != null)
                    successCounter++;
            }
        }

        if (successCounter == 4) {
            System.out.println(
                    "----------------------------------------------DTO PARAMETERS----------------------------------------------");
            System.out.println("Username : " + username + "\t" + "Action : " + action + "\t" + "Cam ID :" + cam_id
                    + "\t" + "Timestamp : " + timestamp + "\n");
            return successMessage;
        } else if (successCounter == 2) {
            System.out.println(
                    "----------------------------------------------DTO PARAMETERS----------------------------------------------");
            System.out.println("\t\tAction : " + action + "\t" + "Cam ID :" + cam_id + "\n");
            return successMessage;
        }
        return failureMessage;
    }
}
