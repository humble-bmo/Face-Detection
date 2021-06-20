import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

camera = cv2.VideoCapture(0) #gets video from default camera

while True:
    ret, frame = camera.read() #reads every frame from webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # makes frame gray for program
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w ,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #ycord_start, ycord_end
        roi_color = frame[y:y+h, x:x+w]

        img_item = "my-image.png" #saves image
        cv2.imwrite(img_item, roi_gray)

        color = (250, 100, 0) #BGR
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        #displays the color frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
