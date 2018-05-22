import takePhotos
import returnPlantSize 
import os
import sys
'''
We should not fail miserably when the program doesnt find a reference object in the photo
'''
PATHTODIRECTORY = os.path.dirname(os.path.realpath("takePhotos"))


def setDirPathByOs():
    OS = sys.platform
    if "linux" in OS:
        PATHTOIMAGES = PATHTODIRECTORY + "/images/"
    else:
        PATHTOIMAGES = PATHTODIRECTORY + "\\images\\"
    return PATHTOIMAGES


picNameTop, picNameSide = takePhotos.takePhotos()
createdImages = takePhotos.getPhotoNames()

top = returnPlantSize.calculateAndDisplay(createdImages[0], 0.955)
side = returnPlantSize.calculateAndDisplay(createdImages[1], 0.955)

os.remove(setDirPathByOs()+"testImage.jpg")

#add imgFileName to measurements
#post to firebase or cache if internet fails

#delete processed images

