from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution=(800,600)

#We should put the following in a function

camera.start_preview()
#TODO the name of the photo should be the date and top camera
#since the top camera will be the PiCam
camera.capture("test1.jpg")
camera.stop_preview()

#TODO make a function for the side camera
#Which will be a USB webcam