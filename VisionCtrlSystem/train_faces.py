import os
import face_recognition
import pickle

known_encodings = []
known_names = []

data_dir = "images"

for person in os.listdir(data_dir):
    person_dir = os.path.join(data_dir, person)
    for img_file in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_file)
        image = face_recognition.load_image_file(img_path)
        encs = face_recognition.face_encodings(image)
        if len(encs) > 0:
            encoding = encs[0]
            known_encodings.append(encoding)
            known_names.append(person)

with open("encodings.pickle", "wb") as f:
    pickle.dump((known_encodings, known_names), f)
