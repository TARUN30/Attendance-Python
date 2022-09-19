import cv2

# Names the window as "Preview"
cv2.namedWindow("preview")

#Names as videocapture after webcam opens
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

#when the rval value is true
while rval:
   #shows image on desktop
    cv2.imshow("preview", frame)
  #vc. is the image reading from the wwebsite
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    #To close webcam
    if key == 27: # exit on ESC
        break

#extracting frames from a video
vc.release()
#destroying the named window    
cv2.destroyWindow("preview")