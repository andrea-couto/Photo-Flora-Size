from picamera import PiCamera
import cv2
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

def takePiCamPhoto(topImgName):
    camera = PiCamera()
    camera.resolution = (800,600)
    camera.capture(topImgName + ".png")

def takeWebcamPhoto(sideImgName):
    cam = cv2.VideoCapture(0)
    s, im = cam.read() # captures image
    sideImgName = sideImgName + ".png"
    cv2.imwrite(sideImgName,im) # writes image to disk

def main ():
    picNameTop = today + "_top"
    picNameSide = today + "_side"
    takePiCamPhoto(picNameTop)
    takeWebcamPhoto(picNameSide)

main()

##TODO save photos to images folder
##These photos should only be stored here until returnPlantSize.py processes them
##after processing returnPlantSize should delete the photos

