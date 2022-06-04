
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:11:26 2021

@author: User
"""

import cv2 as cv
import time
from datetime import datetime
import threading
import sys

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def save(T,no):
    result = datetime.now().strftime("%Y-%m-%d %I-%M-%S %p")
    
    path='./iimg/'+result+'  no.'+str(no)+'.jpg'
    #print(path)
    cv.imwrite(path, T)
    
    #mail(path)
    
'''
設定攝影機編號
'''
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

r=1

while True:
    # Capture frame-by-frame
    t0 = cap.read()[1]

    time.sleep(0.01)
    
    t1 = cap.read()[1]

    # Our operations on the frame come here
    grey1 = cv.cvtColor(t0, cv.COLOR_BGR2GRAY)

    grey2 = cv.cvtColor(t1, cv.COLOR_BGR2GRAY)
    
    
    
    
    blur1 = cv.GaussianBlur(grey1,(7,7),0)
    blur2 = cv.GaussianBlur(grey2,(5,5),0)
    d = cv.absdiff(blur1, blur2)
    ret, th = cv.threshold( d, 10, 255, cv.THRESH_BINARY )
    dilated=cv.dilate(th, None, iterations=1)
    
    
    
    deviation=0
    for i in range(0,480,5):
        for j in range(0,640,5):
            deviation=deviation+dilated[i,j]
    
    D=deviation/10000
    print(D)
    
    text = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    cv.putText(t1, text, (10, 20), cv.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255), 1, cv.LINE_AA)
    
    
    '''
    D就是輸出相片的靈敏度
    '''
    if D>5:   
        print('!!!!!!  ',r,D)
        my_dict = {'T':t1, 'no':r}
        thr=threading.Thread(target=save,kwargs=my_dict)
        thr.start()
        r=r+1
        print(D)
    
    
    '''
    要延遲幾秒? 多一點有縮時攝影的感覺
    '''
    time.sleep(0.2)
    
    
    
    
    # Display the resulting frame
    cv.imshow('frame', t1)
    cv.imshow('kkk',th)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()




