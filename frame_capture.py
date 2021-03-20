#-*- coding: utf-8 -*-
import socket
from picamera import PiCamera
import time
import os

camera = PiCamera()

#for socket connection
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('211.41.203.30',10000))

print("---------Connection complete---------")

count = 0
num = 10 #this is temporary value, should change this number.

while count < num:
    filePath = '/home/pi/Desktop/test'+str(count)+'.jpg'
    camera.capture(filePath)
    
    with open(filePath, 'rb') as file:
            stringData = file.read()
    
    #send to Back-end server through socket
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
    time.sleep(0.5)
    count += 1
    print("count up : "+str(count))
    os.system('rm '+ filePath)
    
print("Capture finished")



