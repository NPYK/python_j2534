#coding:utf-8

import sys
from dllLoader import getDeviceList, load_dll
from dll import *
import ctypes as ct
import Define
import Func

from Error import J2534Error
ptData = PassThru_Data
class ptTxMsg(PassThru_Msg):
    def __init__(self, ProtocolID, TxFlags):
        self.ProtocolID = ProtocolID
        self.TxFlags = TxFlags
    def setData(self, data):
        print data
        self.DataSize = len(data)
        self.Data = ptData()
        for i in range(self.DataSize):
            self.Data[i] = data[i]
    def setIDandData(self, ID, data):
        d = Func.IntToID(ID) + data
        self.setData(d)
class J2534Lib():
    def __init__(self):
        self.DeviceList = getDeviceList()
        self._module = sys.modules[__name__]
    def _setDevice(self, name, dllpath):
        self.name = name
        self.dllPath = dllpath
        self.dll = load_dll(dllpath)
        self.canlib = CanlibDll(self.dll)
    def setDevice(self, num = 0):
        name, dllpath = self.DeviceList[int(num)]
        self._setDevice(name, dllpath)
    def getDeviceList(self):
        return self.DeviceList
    def __getattr__(self, name):
        try:
            return getattr(self.canlib, name)
        except AttributeError:
            raise AttributeError("{t} object has no attribute {n}".format(
                t=str(type(self)), n=name))
j2534lib = J2534Lib()
def ptOpen():
    Name = ''
    DeviceId = ct.c_ulong()
    ret = j2534lib.PassThruOpen(bytes(Name), ct.byref(DeviceId))
    print J2534Error[ret]
    return DeviceId.value
def ptClose(DeviceId):
    """Close Device
    
    Keyword Arguments:
        DeviceId {[int]} -- Device Id Number
    """
    j2534lib.PassThruClose(DeviceId)
def ptConnect(DeviceId, ProtocolID, Flags, BaudRate):
    """Connect

    """
    ChannelID = ct.c_ulong()
    j2534lib.PassThruConnect(DeviceId, ProtocolID, Flags, BaudRate, ct.byref(ChannelID))
    return ChannelID.value
def ptDisconnect(ChannelID):
    """ :TODO
    """
    j2534lib.PassThruDisconnect(ChannelID)
def ptReadMsgs(ChannelID, Msgs, NumMsgs, Timeout):
    """ :TODO
    """
    j2534lib.PassThruReadMsgs(ChannelID, ct.byref(Msgs), ct.byref(NumMsgs), Timeout)
def ptWtiteMsgs(ChannelID, Msgs, NumMsgs, Timeout):
    """[summary]
    
    Arguments:
        ChannelID {[type]} -- [description]
        Msgs {[type]} -- [description]
        NumMsgs {[type]} -- [description]
        Timeout {[type]} -- [description]
    """
    j2534lib.PassThruWriteMsgs(ChannelID, ct.byref(Msgs), ct.byref(NumMsgs), Timeout)
def ptStartPeriodicMsg(ChannelID, Msgs, MsgID, TimeInterval):
    """ :TODO
    """
    j2534lib.PassThruStartPeriodicMsg(ChannelID, ct.byref(Msgs), ct.byref(MsgID), TimeInterval)
def ptStopPeriodicMsg(ChannelID, MsgID):
    """ :TODO
    """
    j2534lib.PassThruStopPeriodicMsg(ChannelID, MsgID)
def ptStartMsgFilter(ChannelID, FilterType, MaskMsg, PatternMsg, FlowControlMsg, MsgID):
    """ :TODO
    """
    j2534lib.PassThruStartMsgFilter(ChannelID, FilterType, ct.byref(MaskMsg), ct.byref(PatternMsg), ct.byref(FlowControlMsg), ct.byref(MsgID))
def ptStopMsgFilter(ChannelID, MsgID):
    """ :TODO
    """
    j2534lib.PassThruStopMsgFilter(ChannelID, MsgID)
def ptSetProgrammingVoltage(DeviceID, PinNumber, Voltage):
    """ :TODO
    """
    j2534lib.PassThruSetProgrammingVoltage(DeviceID, PinNumber, Voltage)
def ptReadVersion(DeviceId):
    """Read Dll Version Msg
    
    Keyword Arguments:
        DeviceId {[int]} -- Device Id Number
    return

    """
    FirmwareVersion = ct.create_string_buffer(80)
    DllVersion = ct.create_string_buffer(80)
    ApiVersion = ct.create_string_buffer(80)
    j2534lib.PassThruReadVersion(DeviceId, FirmwareVersion, DllVersion, ApiVersion)
    return FirmwareVersion.value, DllVersion.value, ApiVersion.value
def ptGetLastError():
    """ :TODO
    """
    ErrorMsg = ct.create_string_buffer(80)
    j2534lib.PassThruGetLastError(ErrorMsg)
    return ErrorMsg.value
def ptIoctl(HandleID, IoctlID, Input, Output):
    """ :TODO
    """
    j2534lib.PassThruIoctl(HandleID, IoctlID, Input, Output)
