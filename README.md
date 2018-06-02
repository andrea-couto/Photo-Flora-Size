"# Photo-Flora-Size"

This project is intended to show plant growth over a period of time using openCV.<br><br>

We wrote this project with raspberry pi in mind, but it will work on windows/linux if the picamera code is removed.<br>
The R.Pi should have a connected piCamera and USB video device.<br>
The piCamera should be mounted above the plant while the USB video device captures an image of the side of the plant.<br>
The background behind the plant should be all white except for a 1"x1" square on the background to the left of the plant on both backgrounds<br>
"onceADay" is programmed to run on the R.Pi using Cron once a day at a given time.<br>
Follow the Cron documentation on how to do this.<br>
"onceADay" will call functions that take photos, analyze them, return the measurements, and post them to firebase.<br>
These measurements are then going to be brought down and graphed using plotly to see growth over time.<br><br>

We ran into some issues installing openCV for python 3 on the raspberry pi. If you want to replicate this project we are considering uploading an .img with openCV preinstalled- keep an eye out for that.<br><br>


Requirements:<br>
openCV-python<br>
scipy<br>
numpy<br>
imutils<br>
firebase_admin<br>

Keep in mind this project is not complete<br><br>
Check out the website: http://andycouto.com/Photo-Flora-Size/<br>




