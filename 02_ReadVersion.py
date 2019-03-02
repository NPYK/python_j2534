#coding:utf-8
import J2534
import sys
J2534.SetErrorLog(True)
devices = J2534.getDevices()

# 
try:
    index = int(sys.argv[1], base=10)
except:
    index = 0

# select index of j2534 device
# PS: 
# 0 {'Name': 'Mongoose ISO', 'FunctionLibrary': 'C:\\WINDOWS\\SysWOW64\\MONGI432.DLL'}
# 1 {'Name': 'ES581.4', 'FunctionLibrary': 'D:\\Program Files (x86)\\Common Files\\ETAS\\J2534 Interface\\ETAS32.dll'}
# 2 {'Name': 'J2534 for Kvaser Hardware', 'FunctionLibrary': 'd:\\Program Files\\Kvaser\\Drivers\\32\\kvJ2534.dll'}
# index = 0  select Mongoose ISO
J2534.setDevice(index)

# open J2534 device
ret, deviceID = J2534.ptOpen()

# read the 
ret, FirmwareVersion, DllVersion, ApiVersion = J2534.ptReadVersion(deviceID)
print ("DLL :", devices[index])
print ("deviceID :",deviceID)
print("FirmwareVersion : %s"%FirmwareVersion)
print("DllVersion : %s"%DllVersion)
print("ApiVersion : %s"%ApiVersion)
# close the device
ret = J2534.ptClose(deviceID)

