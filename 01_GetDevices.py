#coding:utf-8
import J2534
J2534.MethodErrorLog = True
devices = J2534.getDevices()
for id in devices:
    print( id , devices[id])