#coding:utf-8
import J2534
from J2534.Define import *
import sys
J2534.SetErrorLog(True)
devices = J2534.getDevices()
try:
    index = int(sys.argv[1], base=10)
except:
    index = 0
J2534.setDevice(index)

ret, deviceID = J2534.ptOpen()

ret, channelID = J2534.ptConnect(deviceID, ProtocolID.CAN, 0, BaudRate.B500K)


print(channelID)
ret= J2534.ptDisconnect(channelID)
ret = J2534.ptClose(deviceID)

