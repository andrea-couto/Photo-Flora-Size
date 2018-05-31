import takePhotos
import helperFunctions
import returnPlantSize 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import requests

'''
Our convention is posting/pulling top measurement first, then side measurement.

log will be:
DATE HEIGHT WIDTH //for topmeasurement
DATE HEIGHT WIDTH //for sidemeasurement
'''

def checkConnection():
    try:
        resp = requests.get("http://www.firebase.com")
        return resp.status_code        
    except:
         return -1


#add picNametop and picNameSide for adding dates to log
#maybe eventually just posting area of bounding box
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
	lf.close()
	return cachedData


def connectDB(serviceAccountFileName):
	try:
		cred = credentials.Certificate(serviceAccountFileName)
		defaultApp = firebase_admin.initialize_app(cred)
		db = firestore.client()
		return db
	except:
		print("Something went wrong initializing the firebase app")


def postData(db, collectionName, documentName, height, width):
	docRef = db.collection(collectionName).document(documentName)
	docRef.set({
	    u'measurement 1': height,
	    u'measurement 2': width,
	  })


# '''
# We should not fail miserably when the program doesnt find a reference/plant object in the photo
# '''

def main():
	picNameTop, picNameSide = takePhotos.takePhotos()

	topData = returnPlantSize.calculateAndDisplay(picNameTop, 0.955)
	sideData = returnPlantSize.calculateAndDisplay(picNameSide, 0.955)

	#put in function and test to make sure they are 1"x1"
	topRef = topData[0]
	sideRef = sideData[0]

	topMeasurement = topData[1]
	sideMeasurement = sideData[1]

	os.remove(helperFunctions.setDirPathByOs() + picNameSide)
	os.remove(helperFunctions.setDirPathByOs() + picNameTop)


	if (checkConnection() == 200):
		db = connectDB("./serviceAccountKey.json")
		cachedData = ReadLog("TEMPLOG.txt")
# 	#if cachedData.size() !=0:
		#for element in cachedData:
			#for part in element:
				#parts are date, height, width 
				#KEEP IN MIND TOP AND SIDE MEASUREMENTS FOR EACH DATE
				#post parts to firebase

		postData(db, "sideMeasurements", picNameSide, sideMeasurement[0], sideMeasurement[1])
		postData(db, "topMeasurements", picNameTop, topMeasurement[0], topMeasurement[1])

		print( str(sideMeasurement) + " measurement was uploaded")
		print( str(topMeasurement) + " measurement was uploaded")
	else:
		WriteToLog(topMeasurement[0], topMeasurement[1], "TEMPLOG.txt")
		WriteToLog(topMeasurement[0], topMeasurement[1], "TEMPLOG.txt")
		#Add a clear log function?


if __name__ == '__main__':
	main()