import numpy as np
import cv2
import face_recognition as FR
import pickle as pk
import time

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
            
        print("\n=== BURST ENROLLMENT INSTRUCTIONS ===")
        print("1. Center yourself in the camera.")
        print("2. Press SPACE to start the automated capture.")
        print("3. Slowly turn your head as prompted.")
        
        collected_encodings = []
        is_recording = False
        capture_count = 0
        max_captures = 5
        
        last_capture_time = 0
        capture_delay = 2.5 # Wait 1 second between captures

        while True:
            ret, frame = cam.read()
            if not ret:
                print("Couldn't read frame. Please try again.")
                break
                
            frame = cv2.flip(frame, 1)
            
            if not is_recording:
                print("Press SPACE to start")
            else:
                print(f"Capturing: {capture_count}/{max_captures}")
                
            cv2.imshow('Face Enrollment', frame)
            cv2.resizeWindow('Face Enrollment', self.win_l, self.win_h)

            key = cv2.waitKey(1) & 0xFF

            if key == 32 and not is_recording:
                print("\nStarting capture sequence. Move your head slightly between snaps.")
                is_recording = True
                last_capture_time = time.time() 

            if is_recording:
                current_time = time.time()
                
                if current_time - last_capture_time >= capture_delay:
                    print(f"Snap {capture_count + 1} of {max_captures}...")
                    
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    face_locations = FR.face_locations(rgb_frame)
                    
                    if len(face_locations) > 0:
                        encoding = FR.face_encodings(rgb_frame, face_locations)[0]
                        collected_encodings.append(encoding)
                        capture_count += 1
                    else:
                        print("Missed! Keep your face in the frame.")
                    
                    last_capture_time = current_time 

                if capture_count >= max_captures:
                    print("\nProcessing master profile...")
                    
                    master_encoding = np.mean(collected_encodings, axis=0)
                    user_data = {"name": testName, "encoding": master_encoding}
                    
                    with open(file_path, "wb") as f:
                        pk.dump(user_data, f)
                        
                    print(f"Success! Master profile for {testName} saved to {file_path}")
                    break

            elif key == ord('q'):
                print("Exiting without saving.")
                break

        cam.release()
        cv2.destroyAllWindows()
