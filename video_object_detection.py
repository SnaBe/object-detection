# 27-12-2018
# Simon S. Sørensen
# Detect a specific object within a live video feed

# Import OpenCV (cv2), use pip to install modules
import cv2

# Our object cascade from a given path
object_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
# Our default video camera for capture
video_capture = cv2.VideoCapture(0)
# Our line and stroke color - Blue, Green, Red
green_color = (0, 255, 0)
white_color = (255, 255, 255)
stroke = 2
thickness = 1
# Our text font
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.5
# Infinite loop
while True:
    # Capture frame by frame
    return_value, frame = video_capture.read()
    # Convert the captured frame to gray scale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detecting facial features
    faces = object_cascade.detectMultiScale(gray_frame, 1.5, 5)
    # Drawing a rectangle around the detected face
    for (x, y, w, h) in faces:
        # Add up to our face counter
        # The face's x & y position, its width & height in the gray frame (Only for debugging, can be commented out)
        print(x, y, w, h)
        # Region of interest in gray scale & color
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Save an image of our face in gray scale & color
        cv2.imwrite('./images/faces/my-face-gray.png', roi_gray)
        cv2.imwrite('./images/faces/my-face-color.png', roi_color)
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), green_color, stroke)
        # Placeholder for text
        cv2.rectangle(frame, (x, y), (x + 48, y + 20), green_color, cv2.FILLED)
        # Draw text
        cv2.putText(frame, 'Face', (x + 5, y + 15), font, font_scale, white_color, thickness)

    # Display the captured frames
    cv2.imshow('Live video feed', frame)
    # Exit video feed by button press
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release and destroy all when done
video_capture.release()
cv2.destroyAllWindows()
