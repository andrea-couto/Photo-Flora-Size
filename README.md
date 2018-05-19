"# Photo-Flora-Size"

This project is intended to show plant growth over a period of time using openCV.<br><br>

We have a program that will take a photo and reference width as arguments.
returnPlantSize.py uses openCV to recognize the plant in the photo and use a reference
object with a known width in inches to measure the plant.<br><br>

To run returnPlantSize.py in the command line with a photo called plantImage and a quarter as a 
reference object:<br>

python3 returnPlantSize.py --image images/plantImage.jpg --width 0.955<br><br>

Requirements:<br>
openCV-python<br>
scipy<br>
numpy<br>
imutils<br>

takePhoto.py, postToFirebase.py, and test_post.py are incomplete





