# Vision-Based Access Control System

A 3-tier wireless IoT access control system that leverages edge hardware, computer vision, and a scalable backend REST API to automate facial recognition and access logging.

This project evolved from a monolithic, tethered serial architecture (**MK 1.0**) into a fully decoupled, distributed system (**MK 2.0**) utilizing an **ESP32-CAM**, a **Python/OpenCV inference engine**, and a **Java Spring Boot backend**.

## System Architecture (MK 2.0)

The current iteration of the system is divided into three decoupled subsystems to improve scalability and offload computational heavy lifting from the edge hardware:

1. **Hardware / Edge Tier (ESP32-CAM):** Operates purely as a wireless HTTP video streaming server. It captures raw frame data and transmits it over the local network, consuming minimal power and requiring zero on-board ML inference processing.
2. **Inference Engine (Python / OpenCV):** A dedicated Python script that ingests the HTTP video stream. It processes the frames in real time, utilizing a trained Haar Cascade and LBPH (Local Binary Pattern Histogram) model to detect and identify authorized faces.
3. **Backend & Logging (Java Spring Boot):** A RESTful API featuring custom controllers and repository data models. When the Python engine recognizes an authorized face, it issues an HTTP `POST` request to this backend, which securely logs the access event (timestamp, user ID, status) into the database.

## Repository Structure

The repository is organized by system version:

* **`/VisionCtrlSystem_MK_1.0`**: The legacy tethered system utilizing an Arduino UNO, static serial delays, and a tightly coupled Python controller script.
* **`/VisionCtrlSystem_MK_2.0`**: The current production architecture containing the decoupled 3-tier system.

  * **`/ESP_CAM_Files`**: C++ source code and HTTP server configurations for the ESP32-CAM module.
  * **`/FR_engine`**: Python real-time inference scripts.
  * **`/SpringBoot_Files/doorcam`**: The Maven-based Java Spring Boot application.
  * **`/training_scripts`**: Utilities for collecting image data and generating the OpenCV `.yml` training model.

## Prerequisites

To run the MK 2.0 architecture, you will need:

* **Hardware:** ESP32-CAM module, FTDI programmer (for initial flashing), and a 5V power source.
* **Python 3.x:** Required libraries include `opencv-python`, `numpy`, `urllib`, and `requests`.
* **Java 17+ and Maven:** To compile and run the Spring Boot backend.
* **Arduino IDE:** With the ESP32 board manager installed to compile the C++ camera server.

## Installation and Setup (MK 2.0)

### 1. Model Training

Before running the inference engine, you must train the system on authorized faces.

1. Navigate to `VisionCtrlSystem_MK_2.0/training_scripts/`.
2. Add a dataset of authorized faces to a designated training directory, organized by subfolders for each individual.
3. Run `train_faces.py` to generate the compiled training data file, typically an XML or YML file.

### 2. Edge Hardware Deployment

1. Open `VisionCtrlSystem_MK_2.0/ESP_CAM_Files/camera_server.ino` in the Arduino IDE.
2. Update the Wi-Fi credentials (`SSID` and `Password`) to match your local network.
3. Flash the code to the ESP32-CAM module.
4. Open the Serial Monitor to retrieve the device's assigned local IP address.

### 3. Backend Deployment

1. Navigate to the `VisionCtrlSystem_MK_2.0/SpringBoot_Files/doorcam/` directory.

2. Build the project using Maven:

   ```bash
   mvn clean install
   ```

3. Start the Spring Boot server:

   ```bash
   mvn spring-boot:run
   ```

4. The REST API will initialize and begin listening for `POST` requests on port `8080`.

### 4. Running the Inference Engine

1. Navigate to `VisionCtrlSystem_MK_2.0/FR_engine/python_scripts/`.

2. Open `FR_engine_script.py` and update the target URL variable with the IP address retrieved from the ESP32-CAM.

3. Execute the script:

   ```bash
   python FR_engine_script.py
   ```

4. The script will open a live video feed, identify faces against the trained model, and automatically dispatch access logs to the Spring Boot backend.

## Historical Context: MK 1.0

The `MK_1.0` directory contains the initial prototype. This version utilized a standard Arduino tethered via USB to the host computer. The Python script handled facial recognition and communicated via **PySerial** to trigger physical hardware responses.

While functional, the architecture suffered from hardcoded static delays and blocking I/O, ultimately motivating the development of the fully asynchronous and decoupled **MK 2.0** system.
