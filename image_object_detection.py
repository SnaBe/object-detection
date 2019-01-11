# 27-12-2018
# Simon S. Sørensen
# Detect a specific object within a given image, in this case its faces.

# Import OpenCV (cv2), use pip to install
import cv2
# Our image to read from a given path
my_image = cv2.imread('./images/harry-meghan.jpg')
# Our object cascade from a given path
object_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
# Convert the image to gray scale
gray_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
# Detecting facial features in the gray image
faces = object_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# Amount of faces found in an image
face_count = 0
# Drawing a rectangle around the detected faces
for (x, y, w, h) in faces:
    # Add up to our face counter
    face_count += 1
    # The face's x & y position, its width & height in both images (Only for debugging, can be commented out)
    print('Face ' + str(face_count) + ' coordinates: ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h))
    # Region of interest in gray scale & color
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = my_image[y:y+h, x:x+w]
    # Save an image for each face in gray scale and color
    cv2.imwrite('./images/faces/face-' + str(face_count) + '-gray.png', roi_gray)
    cv2.imwrite('./images/faces/face-' + str(face_count) + '-color.png', roi_color)
    # Our line and stroke color - Blue, Green, Red
    color = (0, 255, 0)
    stroke = 2
    # Draw a rectangle around the face(s)
    cv2.rectangle(my_image, (x, y), (x+w, y+h), color, stroke)
    # Save the entire image with the detected face(s)
    cv2.imwrite('./images/all-faces.png', my_image)

# Display the image
cv2.imshow('Your image', my_image)
# Display the image infinitely until any keypress
cv2.waitKey(0)
# Destroy all when done
cv2.destroyAllWindows()
