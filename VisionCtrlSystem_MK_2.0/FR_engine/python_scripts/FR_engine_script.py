import cv2
import face_recognition as FR
import numpy as np
import pickle as pk
import os
import time

espCamVidStream = "http://192.168.1.11:81/stream" #ESP32-CAM stream source

# win_h = 750, win_l = 750
pickle_bin = "/home/abhiram/Workspace/Python_project_files/OpenCV/Security_Sys_Project/Face_Encodings_Bin" #filepath for the face encodings
known_faces = []
known_encodings = []

"""Looping over the face encodings folder:
   Extract names, append to the names list, read pickle files
   Append pickle values to encodings list"""

for filename in os.listdir(pickle_bin):
    if filename.endswith(".pickle"):
        name = filename.removesuffix(".pickle")
        known_faces.append(name)

        full_path = os.path.join(pickle_bin, filename)

        with open(full_path, "rb") as f:
            user_data = pk.load(f)
            name_encoding = user_data["encoding"]
            known_encodings.append(name_encoding)
           
cam = cv2.VideoCapture(espCamVidStream)

if not cam.isOpened():
    print("Could not open camera, please try again.")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Could not read frame.")
        break

    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_locations = FR.face_locations(rgbFrame)
    face_encodings = FR.face_encodings(rgbFrame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = FR.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            match_index = matches.index(True)
            name = known_faces[match_index]

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # cv2.imshow("Security Feed", frame)
    # cv2.resizeWindow("Security Feed", win_l, win_h)

cam.release()
cv2.destroyAllWindows()
