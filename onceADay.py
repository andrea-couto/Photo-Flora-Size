import takePhotos
import returnPlantSize 
import time

'''
We should not fail miserably when the program doesnt find a reference object in the photo
'''

takePhotos.takePhotos()
createdImages = takePhotos.getPhotoNames()

top = returnPlantSize.calculateAndDisplay(createdImages[0], 0.955)
side = returnPlantSize.calculateAndDisplay(createdImages[1], 0.955)

#post to firebase

