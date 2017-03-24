import os
import cv2
import vlc

palm = cv2.CascadeClassifier('palm.xml')
fingertip = cv2.CascadeClassifier('fingertips.xml')
cap = cv2.VideoCapture(0)

flag = True
songplayingBool = False;
string = "Capturing Gesture"
p = vlc.MediaPlayer("/home/dark_knight/Music/Zinda.mp3")
while True:
	ret, inputImage = cap.read()
	grey = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

	palms = palm.detectMultiScale(grey, 1.2, 4)
	fingertips = fingertip.detectMultiScale(grey, 1.2, 4)
	if flag:
		cv2.putText(inputImage, string, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
		i=0
		if songplayingBool:
			for (x, y, h,w) in fingertips:
				i+=1
				if i==2:
					p.pause()
					songplayingBool = False
					flag = False
					string = "Song Paused."
					cv2.putText(inputImage, string, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
		else:
			for (x,y,h,w) in palms:
				i+=1
				if i==1:
					p.play()
					string = "Song Playing"
					cv2.putText(inputImage, string, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
					songplayingBool=True
					flag = False
	cv2.imshow('img', inputImage)
	k=cv2.waitKey(30) & 0xff
	if k==27:
		cap.release()
		cv2.destroyAllWindows()
		break
	if k==65:
		flag = True
#cap.release()
#cv2.destroyAllWindows()