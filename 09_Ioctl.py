#coding:utf-8
import J2534
from J2534.Define import *
import sys

J2534.SetErrorLog(True)


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


ret, vbat = J2534.ReadVbat(ch1)
ret = J2534.ClearTxBuf(ch1)
ret = J2534.ClearRxBuf(ch1)


ret = J2534.ptDisconnect(ch1)
ret = J2534.ptClose(id1)