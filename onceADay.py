import takePhotos
import helperFunctions
import returnPlantSize 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import requests

'''
When reading and writing values from log, firebase, etc. 
we are processing the measurements by top measurement first then 
side measurement. 
When retriecing and posting the data index 0 will be top and 1
will be side

log will be:
DATE HEIGHT WIDTH //for topmeasurement
DATE HEIGHT WIDTH //for sidemeasurement
'''

def checkConnection():
    try:
        resp = requests.get("http://www.google.com")
        return resp.status_code        
    except:
         return -1

#add picNametop and picNameSide for adding dates to log
def WriteToLog(height, width, logFileName):
    lf=open(logFileName,'a')
    lf.write(height + " " + width + "\n")
    lf.close()


def ReadLog(logFileNm):
	cachedData = []
	lf=open(logFileNm)
	for line in lf:
	#TODO break down line into elements
		cachedData.append(line)
	# fn=lf.read()
	lf.close()
	return cachedData

# # Want this running on your pi? 
# # Youll need your own firebase database and serviceAccountKey
cred = credentials.Certificate("./serviceAccountKey.json")
defaultApp = firebase_admin.initialize_app(cred)
db = firestore.client()

# '''
# We should not fail miserably when the program doesnt find a reference/plant object in the photo
# '''

picNameTop, picNameSide = takePhotos.takePhotos()

top = returnPlantSize.calculateAndDisplay(picNameTop, 0.955)
side = returnPlantSize.calculateAndDisplay(picNameSide, 0.955)

#put in function and test to make sure they are 1"x1"
topRef = top[0]
sideRef = side[0]

topMeasurement = top[1]
sideMeasurement = side[1]

os.remove(helperFunctions.setDirPathByOs() + picNameSide)
os.remove(helperFunctions.setDirPathByOs() + picNameTop)


if (checkConnection() == 200):
	cachedData = ReadLog("TEMPLOG.txt")
# 	#if cachedData.size() !=0:
		#for element in cachedData:
			#for part in element:
				#parts are date, height, width 
				#KEEP IN MIND TOP AND SIDE MEASUREMENTS FOR EACH DATE
				#post parts to firebase

	docRefSide = db.collection("sideMeasurements").document(picNameSide)
	docRefSide.set({
	    u'measurement 1': sideMeasurement[0],
	    u'measurement 2': sideMeasurement[1],

	  })
	docRefTop = db.collection("topMeasurements").document(picNameTop)
	docRefTop.set({
	    u'measurement 1': topMeasurement[0],
	    u'measurement 2': topMeasurement[1],

	  })
	print( str(sideMeasurement) + " measurement was uploaded")
	print( str(topMeasurement) + " measurement was uploaded")
else:
	WriteToLog(topMeasurement[0], topMeasurement[1], "TEMPLOG.txt")
	WriteToLog(topMeasurement[0], topMeasurement[1], "TEMPLOG.txt")
	#Add a clear log function?

