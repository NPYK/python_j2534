#coding:utf-8
import J2534
import sys
J2534.SetErrorLog(True)
devices = J2534.getDevices()
try:
    index = int(sys.argv[1], base=10)
except:
    index = 0
J2534.setDevice(index)

ret, deviceID = J2534.ptOpen()
ret, FirmwareVersion, DllVersion, ApiVersion = J2534.ptReadVersion(deviceID)
print ("DLL :", devices[index])
print ("deviceID :",deviceID)
print("FirmwareVersion : %s"%FirmwareVersion)
print("DllVersion : %s"%DllVersion)
print("ApiVersion : %s"%ApiVersion)
ret = J2534.ptClose(deviceID)

