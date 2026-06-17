import numpy as np
import cv2
import face_recognition as FR
import pickle as pk

class face_training:
    def __init__(self, cam_port, win_h, win_l):
        self.cam_port = cam_port
        self.win_h = win_h
        self.win_l = win_l

    def grab_frame(self, file_path, testName):
        cam = cv2.VideoCapture(self.cam_port)

        if not cam.isOpened():
            print("Couldn't open camera. Please try again.")
            exit()
        
        while True:
            ret, frame = cam.read()
            if not ret:
                print("Couldn't read frame. Please try again.")
                break
                
            frame = cv2.flip(frame, 1)

            cv2.imshow('Press SPACE to capture, Q to quit', frame)
            cv2.resizeWindow('Press SPACE to capture, Q to quit', self.win_l, self.win_h)

            key = cv2.waitKey(1) & 0xFF

            if key == 32: 
                print("Processing face...")
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                encodings = FR.face_encodings(rgb_frame)

                if len(encodings) > 0:
                    encoding = encodings[0]
                    user_data = {"name": testName, "encoding": encoding}

                    with open(file_path, "wb") as f:
                        pk.dump(user_data, f)
                    
                    print(f"Success! {testName}'s face saved to {file_path}")
                    break 
                else:
                    print("No face detected! Make sure you are in the frame and try again.")

            elif key == ord('q'):
                print("Exiting without saving.")
                break

        cam.release()
        cv2.destroyAllWindows()
