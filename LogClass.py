#!/usr/bin/env python

#import urequests
import network
import uio
import esp
from machine import RTC
# from timeClass import TimeTank

class Log:
    __resthost = ''
    __deviceid = ''
    __ip = ''
    __rssi = 0
    __currHour = 0
    __currMinute = 0

    # __file = uio.open("tank.log", "a", encoding="utf-8")
    # __output = uio.StringIO()

    def __init__(self, resthost, deviceid):
        self.__resthost = resthost
        self.__deviceid = deviceid

    def __call__(self):
        pass

    def __getip__(self):

        sta_if = network.WLAN(network.STA_IF)
        self.__rssi = sta_if.status('rssi')

        if sta_if.active():
            temp = sta_if.ifconfig()
            self.__ip = temp[0]
        else:
            self.__ip = '0.0.0.0'

    def printl(self, outstring):
        rtc = RTC()
        timeNow = rtc.datetime()
        __currHour = timeNow[4]
        __currMinute = timeNow[5]

        outbuffer = '['
        outbuffer += '\'' + str(__currHour) + ':' + str(__currMinute) + '\', '
        outbuffer += '\'' + self.__deviceid + '\', '
        outbuffer += '\'' + self.__ip + '\', '
        outbuffer += '\'' + str(self.__rssi) + '\', '
        outbuffer += '\'' + str(esp.freemem()) + '\', '
        outbuffer += '\'' + self.__resthost + '\', '
        outbuffer += '\'' + outstring + '\', '
        outbuffer += ']\n'

        f = uio.open("tank.log", "a", encoding="utf-8")
        f.write(outbuffer)
        f.close()

