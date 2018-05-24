from picamera import PiCamera
import cv2
import datetime
import helperFunctions

NOW = datetime.datetime.now()
TODAY = NOW.strftime("%Y-%m-%d")
picNameTop = TODAY + "_top" + ".png"
picNameSide = TODAY + "_side" + ".png"


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


def takePhotos():
    pathToImage = helperFunctions.setDirPathByOs()
    takePiCamPhoto(picNameTop, pathToImage)
    takeWebcamPhoto(picNameSide, pathToImage)
    return picNameTop, picNameSide


if __name__ == '__main__':
    takePhotos()


