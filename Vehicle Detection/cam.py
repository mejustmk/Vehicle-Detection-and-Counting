# Create a VideoCapture object to access the camera
import cv2

def open_camera():
    
    cap = cv2.VideoCapture(0)  # 0 represents the default camera

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to read frame from the camera.")
            break

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()
