#coding:utf-8
import J2534

# open error log 
J2534.SetErrorLog(True)

# collect the J2534 device from the windwos register
devices = J2534.getDevices()

# print all the devices 
for id in devices:
    print( id , devices[id])