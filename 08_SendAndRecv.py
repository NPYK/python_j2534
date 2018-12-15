#coding:utf-8
import J2534
from J2534.Define import *
import sys

J2534.SetErrorLog(False)
import time

BRODCAST_ID = 0x7df
SEND_ID = 0x7e0
RECV_ID = 0x7e8


try:
    index = int(sys.argv[1], base=10)
except:
    index = 0
J2534.setDevice(index)

ret, id1 = J2534.ptOpen()
ret, ch1 = J2534.ptConnect(id1, ProtocolID.ISO15765, 0, BaudRate.B500K)

msg = J2534.ptRxMsg()


maskMsg = J2534.ptMskMsg(0)
maskMsg.setID(0xffffffff)

patternMsg = J2534.ptPatternMsg(0)
patternMsg.setID(SEND_ID)

flowcontrolMsg = J2534.ptPatternMsg(0)
flowcontrolMsg.setID(0x641)

ret, fiterid = J2534.ptStartMsgFilter(ch1, FilterType.FLOW_CONTROL_FILTER,
                                      maskMsg, patternMsg, flowcontrolMsg)

start = time.time()
while True:
    if time.time() - start > 10:
        break
    ret = J2534.ptReadMsgs(ch1, msg, 1, 100)
    if ret is 0:
        msg.show()

ret = J2534.ptDisconnect(ch1)
ret = J2534.ptClose(id1)