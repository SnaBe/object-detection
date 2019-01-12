# 02-01-2018
# Simon S. Sørensen
# Detect a specific object within a live video feed, in this case its faces.

# Import OpenCV (cv2) & numpy as np
import cv2
import numpy as np
# Pillow (PIL) lets us use ImageGrab
from PIL import ImageGrab
# Infinite loop
while True:
    # Our game screen in a fixed bounding box
    # OpenCV only accepts images in a certain format, images as arrays
    # We convert the images grabbed from our screen to an array using numpy
    game_screen = np.array(ImageGrab.grab(bbox=(0, 0, 800, 600)))
    # Convert the game screen to gray for faster processing of object detection
    game_gray = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)
    # Show the screen and convert the colors from BGR to RGB
    cv2.imshow('Game Window', cv2.cvtColor(game_screen, cv2.COLOR_BGR2RGB))
    # Exit screen feed by button press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
# Destroy all when done
cv2.destroyAllWindows()
