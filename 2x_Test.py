#coding:utf-8
import J2534
import sys
import J2534.Define as Define
import ctypes as ct
print J2534.j2534lib.getDeviceList()


J2534.j2534lib.setDevice(int(sys.argv[1]))
id1 = J2534.ptOpen()
print id1
print J2534.ptReadVersion(id1)

ch1 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch2 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch3 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch4 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch5 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
print ch1, ch2, ch3,ch4,ch5
data = [ 0x00, 0x00, 0x07, 0xdf, 0x01, 0x02, 0x01, 0x02, 0x01, 0x02]
msg = J2534.ptTxMsg(Define.ISO15765, Define.ISO15765_FRAME_PAD)

#msg.setData(data)
msg.setIDandData(0x7df, [1,2,3,4,5,6,7])
J2534.ptWtiteMsgs(ch1, msg, ct.c_ulong(1), 100)

J2534.ptDisconnect(ch1)
J2534.ptDisconnect(ch2)
J2534.ptDisconnect(ch3)
J2534.ptDisconnect(ch4)
J2534.ptDisconnect(ch5)
J2534.ptClose(id1)
