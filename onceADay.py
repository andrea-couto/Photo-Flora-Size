import takePhotos
import helperFunctions
import returnPlantSize 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Want this running on your pi? 
# Youll need your own firebase database and serviceAccountKey
cred = credentials.Certificate("./serviceAccountKey.json")
defaultApp = firebase_admin.initialize_app(cred)
db = firestore.client()

'''
We should not fail miserably when the program doesnt find a reference/plant object in the photo
'''

picNameTop, picNameSide = takePhotos.takePhotos()

top = returnPlantSize.calculateAndDisplay(createdImages[0], 0.955)
side = returnPlantSize.calculateAndDisplay(picNameSide, 0.955)

#put in function and test to make sure they are 1"x1"
topRef = top[0]
sideRef = side[0]

topMeasurement = top[1]
sideMeasurement = side[1]

#TODO check internet connection
#cache top and side if internet fails
docRef = db.collection("sideMeasurements").document(picNameSide)
docRef.set({
    u'measurement 1': sideMeasurement[0],
    u'measurement 2': sideMeasurement[1],

  })
# print(+ " measurement was uploaded")

os.remove(helperFunctions.setDirPathByOs() + picNameSide)

# post to log
