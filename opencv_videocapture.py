# This is to take live video
##import cv2
##
##capture=cv2.VideoCapture(0)
##while True:
##    status, frame = capture.read()
##    cv2.imshow('video',frame)
##    if cv2.waitKey(3) & 0xFF == ord('q'):
##        break
##capture.release()
##cv2.destroyAllWindows()

#This is to take a screen Shot
##import cv2
##
##capture=cv2.VideoCapture(0)
##while True:
##    _, frame = capture.read()
##    cv2.imshow('video',frame)
##    if cv2.waitKey(3) & 0xFF == ord('q'):
##        break
##    if cv2.waitKey(3) == ord('s'):
##        print('sasank')
##        cv2.imwrite('screenshot.png',frame)
##capture.release()
##cv2.destroyAllWindows()

##1.)
##num=1
##while num<=10:
##    print('sasank'+str(num))
##    num+=1

##2.)
##num=1
##while True:
##    while num<=10:
##        print(num)
##        num+=1
##        if num == 10:
##            break
##    while num>=1:
##        print(num)
##        num-=1
##        if num == 1:
##            break

##2.)(with only one while loop)
##num=1
##changeby=1
##while True:
##    if num<=10:
##        print(num)
##        num=num+changeby
##    if num ==10:
##        changeby=-1
##    if num == 1:
##        changeby=1
    

##3.)
import cv2

capture=cv2.VideoCapture(0)
num=1
activation = False
while num<=500:
    
    abc, frame = capture.read()
    cv2.rectangle(frame,(625,0),(1250,500),(255,0,0),2)
    grayframe=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ROI=grayframe[0:500,625:1250]
    cv2.imshow('video',grayframe)

    if cv2.waitKey(3) == ord('s'):
        print('activated')
        activation = True
    if activation == True:
        ROI=cv2.resize(ROI,(28,28))
        
        cv2.imwrite('RockPaperScissors/Scissors/scissors'+str(num)+'.png',ROI)
        num=num+1
    
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
