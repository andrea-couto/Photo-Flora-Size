# from picamera import PiCamera
import cv2
import datetime
import os
import sys

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
picNameTop = today + "_top" + ".png"
picNameSide = today + "_side" + ".png"
PATHTODIRECTORY = os.path.dirname(os.path.realpath("takePhotos"))

def setDefaultsByOs():
    OS = sys.platform
    pathToImage = ""
    if "linux" in OS:
        pathToImage = PATHTODIRECTORY + "/images/"
    else:
        pathToImage = PATHTODIRECTORY + "\\images\\"
    return pathToImage

def takePiCamPhoto(topImgName, pathToImage):
    camera = PiCamera()
    camera.resolution = (800,600)
    camera.capture(pathToImage + topImgName)

def takeWebcamPhoto(sideImgName, pathToImage):
    cam = cv2.VideoCapture(0)
    s, im = cam.read() 
    sideImgName = sideImgName
    #TODO error check writing pathToImage
    cv2.imwrite(pathToImage + sideImgName,im)

def getPhotoNames():
    return picNameTop, picNameSide


def takePhotos():
    pathToImage = setDefaultsByOs()
    # takePiCamPhoto(picNameTop, pathToImage)
    takeWebcamPhoto(picNameSide, pathToImage)


if __name__ == '__main__':
    takePhotos()


