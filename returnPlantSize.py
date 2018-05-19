# This program draws heavily upon the following tutorial
# https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/

import cv2
import numpy as np
import argparse
from scipy.spatial import distance as dist
from imutils import contours
import imutils
from imutils import perspective

'''
maybe we shoud'nt be taking the image as a parameter because we dont know what the image name will be
how about we grab a list of all the images in the images folder, then while list is not empty,
we take the image and process it, then delete it when done processing. '''

#Global Constants
lowerBound = np.array([33, 80, 40])
upperBound = np.array([102, 255, 255])
kernelOpen = np.ones((1, 1))
kernelClose = np.ones((20, 20))

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def makeCommandArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    ap.add_argument("-w", "--width", type=float, required=True,
                    help="width of the left-most object in the image (in inches)")
    args = vars(ap.parse_args())
    return args

def returnGreenObjects(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    maskFinal = maskClose
    _, conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return conts

def returnReferenceObject(img):
    gray = cv2.GaussianBlur(img, (7, 7), 0)
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    Othercnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ref = Othercnts[0] if imutils.is_cv2() else Othercnts[1]
    ref = ref[0]
    return ref

def computeBoundingBox(contobj):
    box = cv2.minAreaRect(contobj)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    return box

def computeTopBottomMidpoints(tl, tr, bl, br):
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    return (tltrX, tltrY), (blbrX, blbrY)

def computeSideMidpoints(tl, tr, bl, br):
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    return (tlblX, tlblY), (trbrX, trbrY)

def drawMidpoints(orig, tltrX, tltrY, tlblX, tlblY,blbrX,blbrY,trbrX,trbrY):
    cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

def drawMidpointLines(orig, tltrX, tltrY, blbrX, blbrY,tlblX,tlblY,trbrX,trbrY):
    cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
             (255, 0, 255), 2)
    cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
             (255, 0, 255), 2)

def main():
    args = makeCommandArguments()
    img = cv2.imread(args["image"],1)
    img = cv2.resize(img, (340, 220))

    conts = returnGreenObjects(img)
    ref = returnReferenceObject(img)

    (cnts, _) = contours.sort_contours(conts)
    pixelsPerMetric = None

    cnts = (ref,) + cnts

    for contobj in cnts:
        if cv2.contourArea(contobj) < 100:
            continue
        orig = img.copy()
        box = computeBoundingBox(contobj)

        # order points top-left, top-right, bottom-right, and bottom-left
        box = perspective.order_points(box)
        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

        for (x, y) in box:
            cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
            (tl, tr, br, bl) = box
            (tltrX, tltrY), (blbrX, blbrY) = computeTopBottomMidpoints(tl, tr, bl, br)
            (tlblX, tlblY), (trbrX, trbrY) = computeSideMidpoints(tl, tr, bl, br)
            drawMidpoints(orig, tltrX, tltrY, tlblX, tlblY,blbrX,blbrY,trbrX,trbrY)
            drawMidpointLines(orig, tltrX, tltrY, blbrX, blbrY,tlblX,tlblY,trbrX,trbrY)

            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

            if pixelsPerMetric is None:
                pixelsPerMetric = dB / args["width"] #in inches

            # compute the size of the object
            dimA = dA / pixelsPerMetric
            dimB = dB / pixelsPerMetric

            # draw the object sizes on the image
            cv2.putText(orig, "{:.1f}in".format(dimB),
                        (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (0, 0, 0), 2)

            cv2.putText(orig, "{:.1f}in".format(dimA),
                        (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (0, 0, 0), 2)
            
        print(str(round(dimA,2)) + " " + str(round(dimB,2)))


        cv2.imshow("final", orig)
        cv2.waitKey(0)

'''This needs to run once for top and once for side cam
the posting really should be done in another file
This can return the sizes and be called in postToFirebase.py

topCam = returnPlantSize(topImage.jpg,0.955)
sideCam = returnPlantSize(sideImage.jpg,0.955)

#post to doc topImage
#post to doc SideImage

'''


main()
