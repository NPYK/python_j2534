#coding:utf-8
from wrapper import *
from prettytable import PrettyTable
from Define import *
__version__ = '0.1'


def getDeviceList():
    devices = j2534lib.getDeviceList()
    table = PrettyTable( ['ID','DeviceName', 'Device Dll Path'] )
    i = 0
    for device in devices:
        table.add_row( [ i, device[0], device[1] ] )
        i = i +1
    print '\nDevices:\n'
    print table
def CheckConnect(id):
    id = int(id)
    j2534lib.setDevice(id)
    ret, deviceID = ptOpen()
    if ret == 0x00:
        ret, ch1 = ptConnect(deviceID, ISO15765, 0, 500000)
        ptDisconnect(ch1)
        if ret == 0x00:
            return 'Device has Connect'
    ptClose(deviceID)
    return 'Device Not Connect'
def GetDeviceVersion( id ):
    id = int(id)
    j2534lib.setDevice(id)
    ret, deviceID = ptOpen()
    ret, firmVersion, DllVersion, ApiVersion = ptReadVersion(deviceID)
    ptClose(deviceID)
    return firmVersion, DllVersion, ApiVersion
def GetInfo():
    dlllist = j2534lib.getDeviceList()
    devices = dict()
    for id in range(len(dlllist)):
        devices[id] = dict()
        devices[id]['ID'] = id
        devices[id]['DeviceName'] = dlllist[id][0]
        devices[id]['Device DLL Path'] = dlllist[id][1]
        firmVersion, DllVersion, ApiVersion = GetDeviceVersion( id )
        devices[id]['Firmware Version'] = firmVersion
        devices[id]['Dll Version'] = DllVersion
        devices[id]['Api Version'] = ApiVersion
        devices[id]['If Connect'] = CheckConnect(id)
    namelist = ['ID','DeviceName', 'Device DLL Path', 'Firmware Version', 'Dll Version', 'Api Version', 'If Connect']
    table = PrettyTable( namelist )
    i = 0
    for id in range(len(dlllist)):
        row = list()
        for n in namelist:
            row.append(devices[id][n])
        table.add_row( row )
    print '\nDevices:\n'
    print table
print GetInfo()