# Vision-Based Access Control System

A prototype access control system that uses computer vision to make identity-based access decisions and actuates a physical locking mechanism through embedded control logic.

## What this project does
- Detects and recognizes faces from a camera feed using OpenCV
- Matches detected faces against a locally maintained face database
- Controls a servo-based locking mechanism via Arduino based on recognition outcome
- Displays system state and access status on an LCD interface

## System overview
A camera feed is processed using OpenCV-based face recognition. Recognition results are converted into control signals that are sent to an Arduino, which drives a servo motor acting as a lock. An LCD provides real-time feedback on system state and access decisions.

## Tech stack
- Python
- OpenCV
- Arduino
- Servo motor
- LCD interfacing

## Current status
This repository contains a stable, device-local prototype focused on vision-to-actuation integration. Networking and backend services are intentionally out of scope at this stage.
