import cv2
 
camera = cv2.VideoCapture(0)
 
if not camera.isOpened():
    print("Could not open the camera")
else:
    print("Press S to save a picture. Press Q to quit.")
 
    while True:
        success, frame = camera.read()
 
        if not success:
            print("Could not read a camera frame")
            break
 
        cv2.imshow("My camera", frame)
        key = cv2.waitKey(1) & 0xFF
 
        if key == ord("s"):
            cv2.imwrite("camera_picture.jpg", frame)
            print("Saved camera_picture.jpg")
 
        if key == ord("q"):
            break
 
camera.release()
cv2.destroyAllWindows()