import sys
import os

PATHTODIRECTORY = os.path.dirname(os.path.realpath("takePhotos"))

def setDirPathByOs():
    OS = sys.platform
    if "linux" in OS:
        PATHTOIMAGES = PATHTODIRECTORY + "/images/"
    else:
        PATHTOIMAGES = PATHTODIRECTORY + "\\images\\"
    return PATHTOIMAGES