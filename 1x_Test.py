#coding:utf-8
import J2534

print J2534.j2534lib.getDeviceList()

J2534.j2534lib.setDevice(2)
id1 = J2534.ptOpen()
id2 = J2534.ptOpen()
id3 = J2534.ptOpen()
print id1, id2, id3
print J2534.ptReadVersion(id1)

ch1 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch2 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch3 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
ch4 = J2534.ptConnect(id1, J2534.ISO15765, 0, 500000)
print ch1, ch2, ch3,ch4 


J2534.ptDisconnect(ch1)
J2534.ptDisconnect(ch2)
J2534.ptDisconnect(ch3)
J2534.ptDisconnect(ch4)
J2534.ptClose(id1)
J2534.ptClose(id2)
J2534.ptClose(id3)