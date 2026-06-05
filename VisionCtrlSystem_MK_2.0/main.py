from train_faces import face_training
import os
import pickle as pk

def main():
    print("===FACE TRAINING SCRIPT===")
    print("Press Q to exit ")

    print("Please enter the required variables: (Camera Port, Window Height, Window Length)")
    cam_p = int(input("Enter the camera port"))
    w_h = int(input("Enter the window height"))
    w_l = int(input("Enter the window length"))

    ft = face_training(cam_port=cam_p, win_h=w_h, win_l=w_l)

    directory = os.makedirs("Face_Encodings_Bin", exist_ok=True)
    testSubjectName = input("Please enter the test subject's name: ").strip()
    filePath = os.path.join("Face_Encodings_Bin", f"{testSubjectName}.pickle")

    ft.grab_frame(filePath, testSubjectName)

if __name__ == "__main__":
    main()