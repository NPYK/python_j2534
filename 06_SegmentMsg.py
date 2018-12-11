#coding:utf-8
import J2534
from J2534.Define import *
import sys

J2534.SetErrorLog(True)
import time

try:
    index = int(sys.argv[1], base=10)
except:
    index = 0
J2534.setDevice(index)

J2534.setDevice(key=index)
ret, id1 = J2534.ptOpen()
ret, ch1 = J2534.ptConnect(id1, ProtocolID.ISO15765, 0, 500000)

msg = J2534.ptTxMsg(ProtocolID.ISO15765, 32)

data = [2,10,3,0,0,0,0,0,0]
#data = data + [0]*padding(len(data))
msg.setIDandData(0x241, data )


maskMsg = J2534.ptMskMsg(16)
maskMsg.setID(0xffffffff)

patternMsg = J2534.ptPatternMsg(16)
patternMsg.setID(0x641)

flowcontrolMsg = J2534.ptPatternMsg(16)
flowcontrolMsg.setID(0x241)

ret, fiterid = J2534.ptStartMsgFilter(ch1, FilterType.FLOW_CONTROL_FILTER,
                                      maskMsg, patternMsg, flowcontrolMsg)

ret = J2534.ptWtiteMsgs(ch1, msg, 1, 100)
time.sleep(3)

ret = J2534.ptDisconnect(ch1)
ret = J2534.ptClose(id1)