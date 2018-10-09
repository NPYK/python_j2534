#coding:utf-8
import J2534
import sys
import J2534.Define as Define
import ctypes as ct



devices = J2534.j2534lib.getDeviceList()
for i in devices:
    print i

J2534.j2534lib.setDevice(int(sys.argv[1]))
ret, id1 = J2534.ptOpen()
print id1
print 'OpenError:', J2534.Error[ret]


ret, ch1 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
print 'ConnectError:', J2534.Error[ret]
print 'Channel Id:', ch1

if ret is 0x00:
    msg = J2534.ptTxMsg(Define.ISO15765, Define.ISO15765_FRAME_PAD)
    msg.setIDandData(0x7df, [1, 2, 3, 4, 5, 6, 7])
    ret = J2534.ptWtiteMsgs(ch1, msg, ct.c_ulong(1), 100)
    print 'Send Error:', J2534.Error[ret]

ret = J2534.ptDisconnect(ch1)
print 'Disconnect Error:', J2534.Error[ret]
ret = J2534.ptClose(id1)
print 'Close Error:', J2534.Error[ret]
