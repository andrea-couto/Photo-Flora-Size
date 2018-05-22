from picamera import PiCamera
import cv2
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
picNameTop = today + "_top" + ".png"
picNameSide = today + "_side" + ".png"

def takePiCamPhoto(topImgName):
    camera = PiCamera()
    camera.resolution = (800,600)
    camera.capture(topImgName)

def takeWebcamPhoto(sideImgName):
    cam = cv2.VideoCapture(0)
    s, im = cam.read() 
    sideImgName = sideImgName
    cv2.imwrite(sideImgName,im)

def getPhotoNames():
    return picNameTop, picNameSide


def takePhotos():
    takePiCamPhoto(picNameTop)
    takeWebcamPhoto(picNameSide)
    

if __name__ == '__main__':
    takePhotos()


