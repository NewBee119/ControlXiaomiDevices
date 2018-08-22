#! /usr/bin/env python
#coding=utf-8

from miio.airpurifier import AirPurifier
#from miio.device import	Device
import time

ip = '192.168.9.150'
token = '62fc6a0729ef7c1d97662d4ab8d75708'
			  
a1= AirPurifier(ip, token)

while 1:
    time.sleep(2)
    a1.off()
    time.sleep(2)
    a1.on()