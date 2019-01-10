# 27-12-2018
# Simon S. Sørensen
# Detect a specific object within a live video feed

# Import OpenCV (cv2) & numpy as np, use pip to install
import cv2
# Our object cascade from a given path
object_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
# Our default video camera for capture
video_capture = cv2.VideoCapture(0)
# Infinite loop
while True:
    #  Capture frame by frame
    return_value, frame = video_capture.read()
    # Convert the captured frame to gray scale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #  Detecting facial features
    faces = object_cascade.detectMultiScale(gray_frame, 1.5, 5)
    # Drawing a rectangle around the detected face
    for (x, y, w, h) in faces:
        # The face's x & y position, its width & height in the gray frame (Only for debugging, can be commented out)
        print(x, y, w, h)
        # Region of interest in gray scale & color
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Save an image of our face in gray scale & color
        cv2.imwrite('./images/faces/my-face-gray.png', roi_gray)
        cv2.imwrite('./images/faces/my-face-color.png', roi_color)
        # Our line and stroke color - Blue, Green, Red
        color = (0, 255, 0)
        stroke = 2
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)

    # Display the captured frames
    cv2.imshow('Live video feed', frame)
    # Exit video feed by button press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release and destroy all when done
video_capture.release()
cv2.destroyAllWindows()
