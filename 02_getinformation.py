#coding:utf-8

import J2534


print J2534.j2534lib.getDeviceList()

J2534.j2534lib.setDevice(1)
deviceID = J2534.ptOpen()
a,b,c = J2534.ptReadVersion(deviceID)

print deviceID
print a, b ,c