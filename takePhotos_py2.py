# from picamera import PiCamera
import cv2

# camera = PiCamera()
# camera.resolution=(800,600)

# #We should put the following in a function

# camera.start_preview()
# #TODO the name of the photo should be the date and top camera
# #since the top camera will be the PiCam
# camera.capture("test1.jpg")
# camera.stop_preview()

#TODO make a function for the side camera
#Which will be a USB webcam

cam = cv2.VideoCapture(0)
s, im = cam.read() # captures image
##cv2.imshow("Test Picture", im) # displays captured image
cv2.imwrite("test.png",im) # writes image test.bmp to disk
