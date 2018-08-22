#! /usr/bin/env python
#coding=utf-8

from yeelight import Bulb
from yeelight import discover_bulbs
import time

print discover_bulbs()
bulb = Bulb("192.168.9.151")

while 1:
    try:
        bulb.turn_on()
        time.sleep(2)
        bulb.turn_off()
        time.sleep(2)
    except:
        continue