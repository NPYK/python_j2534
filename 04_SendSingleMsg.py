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

ret, deviceID = func.ptOpen()

ret, channelID = func.ptConnect(deviceID, ProtocolID.CAN, 0, BaudRate.B500K)

msg = J2534.ptTxMsg(ProtocolID.CAN, 0)
msg.setIDandData(0x123, [0,1,2,3,4,5,6,7])

func.ptWtiteMsgs(channelID, msg, 1, 100)

ret = func.ptDisconnect(channelID)
ret = func.ptClose(deviceID)
