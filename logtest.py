#!/usr/bin/env python

import uos, uio, machine, ubinascii
from LogClass import Log
from timeClass import TimeTank
import ssd1306

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)


def getdeviceid():

    deviceid = ubinascii.hexlify(machine.unique_id()).decode()
    deviceid = deviceid.replace('b\'', '')
    deviceid = deviceid.replace('\'', '')

    return deviceid


restHost = 'http://harwoods.no-ip.org:5000'
deviceid = getdeviceid()

mytime = TimeTank(deviceid)
while not mytime.settime():
    pass

log = Log(restHost, deviceid)

log.printl('This is a small step for man')
log.printl('a giant leap for mankind')

print(uos.listdir())

