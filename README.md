# object-detection

Detect specific objects in images, video feed and games using [OpenCV ](https://opencv.org/ "Opencv.org") (Open Source Computer Vision Library) & [Python 3](https://www.python.org/downloads/ "Python.org"). Here's a list of the current scripts. Some are incomplete or for specific platforms.

### 1. Images can be JPEG, JPG, PNG or other commonly used image file types.

Add our images file path (Tested on Windows & Linux)
```
my_image = cv2.imread('./images/harry-meghan.jpg')
```
Run the image script 

```
$ py image_object_detection.py
```
### 2. Video feed can come trough USB or camera modules. 

Our default video camera for capture (Tested on Winndows, Mac & Linux)
```
video_capture = cv2.VideoCapture(0)
```
Pi Camera module (Tested on Raspberry Pi 3 B+)
```
# PiCam settings
camera = PiCamera()
camera.resolution(640, 360)
camera.framerate(30)

# Video capture
video_capture = PiRGBArray(camera, (640, 360))
```
Run the picam script 

```
$ python video_object_detection_with_picam.py
```

### 3. Game capture is taken from a specific position on the primary screen.

Our game screen to capture (Tested on Winndows)
```
game_screen = np.array(ImageGrab.grab(bbox=(0, 0, 800, 600)))
```
Run the game script 

```
$ py game_object_detection.py
```
