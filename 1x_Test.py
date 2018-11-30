#coding:utf-8
from J2534 import j2534lib
from J2534 import wrapper as func
from J2534.Define import *
from J2534.Error import printerr
import sys
print(j2534lib.getDevices())


j2534lib.setDevice(key=int(sys.argv[1]))
ret, id1 = func.ptOpen()

print(id1)
ret, FirmwareVersion, DllVersion, ApiVersion = func.ptReadVersion(id1)
print("FirmwareVersion : %s"%FirmwareVersion)
print("DllVersion : %s"%DllVersion)
print("ApiVersion : %s"%ApiVersion)
ret, ch1 = func.ptConnect(id1, ProtocolID.CAN, 0, 500000)
print(ch1)
func.ptDisconnect(ch1)
func.ptClose(id1)
