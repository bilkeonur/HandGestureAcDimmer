import math
import cv2
import mediapipe as mp
import time
import serial
import threading

#On MacOS /dev/cu.HC-05 is bluetooth port name or Windows ex. COM4
bluetooth=serial.Serial("/dev/tty.usbserial-A5XK3RJT", 9600, timeout=.1)
#bluetooth=serial.Serial("/dev/cu.HC-05", 9600, timeout=.1)


print("Bluetooth Connected")

cap = cv2.VideoCapture(0)
 
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
 
pTime = 0
cTime = 0
 
stX = 0
stY = 0
enX = 0
enY = 0

while True:
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
 
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:
                    cv2.circle(img, (cx, cy), 20, (255, 0, 0), cv2.FILLED)
                    stX = cx
                    stY = cy
                    
                if id == 8:
                    cv2.circle(img, (cx, cy), 20, (255, 0, 0), cv2.FILLED)
                    enX = cx
                    enY = cy
                    
                #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (stX, stY), (enX, enY), (0, 0, 255), 3)
 
            #mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
 
    val1 = math.pow((enX-stX),2)
    val2 = math.pow((enY-stY),2)
    diff = math.sqrt(val1+val2)
    
    if diff >= 300:
        diff = 300
        
    if diff <= 80:
        diff = 80
    
    perc = int(((diff - 80) / (300 - 80) ) * (100 - 0) + 0)

    dimVal = int(120 - (perc*1.2))

    bluetooth.write(chr(dimVal).encode())
    
    cv2.putText(img, str(perc), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)