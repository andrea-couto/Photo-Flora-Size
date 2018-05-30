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

top = returnPlantSize.calculateAndDisplay(picNameTop, 0.955)
side = returnPlantSize.calculateAndDisplay(picNameSide, 0.955)

#put in function and test to make sure they are 1"x1"
topRef = top[0]
sideRef = side[0]

topMeasurement = top[1]
sideMeasurement = side[1]

#TODO check internet connection
#cache top and side if internet fails
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

os.remove(helperFunctions.setDirPathByOs() + picNameSide)
os.remove(helperFunctions.setDirPathByOs() + picNameTop)

# post to log

