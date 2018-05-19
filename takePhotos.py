from picamera import PiCamera
import cv2

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
    testNameTop = "testName"
    testNameSide = "testSideName"
    takePiCamPhoto(testNameTop)
    takeWebcamPhoto(testNameSide)

main()

##TODO give descriptive names to photos

##TODO save photos to images folder
##These photos should only be stored here until returnPlantSize.py processes them
##after processing returnPlantSize should delete the photos

