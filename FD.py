import cv2  #importing cv2 libirary
import imutils #import imutils lib

alg="haarcascade_frontalface_default.xml"  #import a model
haar_cascade=cv2.CascadeClassifier(alg) #Loading A Model
cam=cv2.VideoCapture(1) #initializing Camera

while True:
     _,img=cam.read() #read Frame from the Camera
     
     grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to the gray image
     face=haar_cascade.detectMultiScale(grayImg,1.1,4)#Get Coordinate 1.1 - scaling factor 4-neigbour pixle
     for (x,y,w,h) in face:
          cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),2)
          cv2.imshow("VideoStream",img)
     if cv2.waitKey(1) & 0xFF == 27:
          break
cam.release()
cv2.destroyAllWindows()
     