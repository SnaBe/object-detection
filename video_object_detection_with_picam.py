# 07-01-2018
# Simon S. Sørensen
# Detect a specific object within a live video feed from a PiCam

# Import OpenCV (cv2) & PiCamera modules, use pip to install modules
import cv2
from time import sleep
from picamera import PiCamera
from picamera.array import PiRGBArray

# Our object cascade from a given path
object_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

width = 1280
height = 720

# PiCam settings
camera = PiCamera()
camera.resolution = (width, height)
camera.framerate = 30
# Video capture
video_capture = PiRGBArray(camera, size=(width, height))

# Let the camera warm up
sleep(0.1)

# Start video frame capture
for still in camera.capture_continuous(video_capture, format='bgr', use_video_port=True):
    # Frame as an array
    image = still.array
    # Convert image to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detecting facial features
    faces = object_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Drawing a rectangle around the detected face
    for(x, y, w, h) in faces:
        # Draw the rectangle
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Text placeholder
        cv2.rectangle(image, (x, y), (x + 48, y + 26), (0, 255, 0), cv2.FILLED)
        # Draw text
        cv2.putText(image, 'Face', (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Show the captured frames
    cv2.imshow('PiCam Live video feed', image)

    # Clear the video capture
    video_capture.truncate(0)

    # Exit video feed by button press (q in this case)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Destroy all when done
cv2.destroyAllWindows()
