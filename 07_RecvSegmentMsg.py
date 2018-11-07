#coding:utf-8
from J2534 import j2534lib
from J2534 import wrapper as func
from J2534.Define import *
from J2534.Error import printerr
import time
devices = j2534lib.getDevices()
print( devices) 
device = devices[2]
j2534lib.setDevice(key = 2)
ret, id1 = func.ptOpen()
printerr(ret)
ret, ch1 = func.ptConnect(id1, ProtocolID.ISO15765, 0, 500000)
printerr(ret)

msg = func.ptRxMsg()


maskMsg = func.ptMskMsg(0)
maskMsg.setID(0xffffffff)

patternMsg = func.ptPatternMsg(0)
patternMsg.setID(0x241)

flowcontrolMsg = func.ptPatternMsg(0)
flowcontrolMsg.setID(0x641)

ret, fiterid = func.ptStartMsgFilter(ch1, FilterType.FLOW_CONTROL_FILTER ,maskMsg, patternMsg, flowcontrolMsg)
printerr(ret)

start = time.time()
while True:
    if time.time() - start > 10:
        break
    ret = func.ptReadMsgs(ch1, msg, 1, 100)
    if ret is 0:
        msg.show()

ret = func.ptDisconnect(ch1)
printerr(ret)
ret = func.ptClose(id1)
printerr(ret)