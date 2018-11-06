#coding:utf-8
from J2534 import j2534lib
from J2534 import wrapper as func
from J2534.Define import *
from J2534.Error import printerr
devices = j2534lib.getDevices()
print( devices) 
device = devices[1]
j2534lib.setDevice(key = 1)
print(1)
ret, id1 = func.ptOpen()
printerr(ret)
ret, ch1 = func.ptConnect(id1, ProtocolID.CAN, 0, 500000)
printerr(ret)

msg = func.ptTxMsg(ProtocolID.CAN, 0)

msg.setIDandData(0x123, [0,1,2,3,4,5,6,7])

func.ptWtiteMsgs(ch1, msg, 1, 100)

ret = func.ptDisconnect(ch1)
printerr(ret)
ret = func.ptClose(id1)
printerr(ret)