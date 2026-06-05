import cv2
import face_recognition
import pickle
import serial
import time

ser = serial.Serial("COM8", 9600)  # or /dev/ttyUSB0 on linux
time.sleep(2)

with open("encodings.pickle","rb") as f:
    known_encs, known_names = pickle.load(f)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    unlocked = False

    for (top,right,bottom,left), enc in zip(faces, encodings):
        matches = face_recognition.compare_faces(known_encs, enc)
        if True in matches:
            idx = matches.index(True)
            name = known_names[idx]
            print("seen", name)
            unlocked = True
            break

    if unlocked:
        ser.write(b"1")
    else:
        ser.write(b"0")

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
