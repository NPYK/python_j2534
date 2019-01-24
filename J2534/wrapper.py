#coding:utf-8

import sys
import J2534.dllLoader as dllloader
from J2534.dll import *
import ctypes as ct
from J2534.Define import *
import J2534.Func as Func
from J2534.Error import showErr

ptData = PassThru_Data
class baseMsg(PassThru_Msg):
    def _setData(self, data):
        print (data)
        self.DataSize = len(data)
        self.Data = ptData()
        for i in range(self.DataSize):
            self.Data[i] = data[i]
    def setID(self, ID):
        d = Func.IntToID(ID)
        self._setData(d)
    def setIDandData(self, ID, data = []):
        d = Func.IntToID(ID) + data
        self._setData(d)

class pt15765Msg(baseMsg):
    def __init__(self, TxFlag):
        self.ProtocolID = ProtocolID.ISO15765
        self.TxFlags = TxFlag
class ptMskMsg(pt15765Msg):
    pass
class ptPatternMsg(pt15765Msg):
    pass
class ptFlowControlMsg(pt15765Msg):
    pass
class ptTxMsg(baseMsg):
    def __init__(self, ProtocolID, TxFlags):
        self.ProtocolID = ProtocolID
        self.TxFlags = TxFlags
class ptRxMsg(baseMsg):
    def show(self):
        print(self.ProtocolID, self.RxStatus, self.Data[:self.DataSize])

class GetParameter(SCONFIG_LIST, Parameter):
    def __init__(self):
        self.NumOfParams = len(Parameter.USED)
        self.paras = SCONFIG * self.NumOfParams
        for i in range(self.NumOfParams):
            self.paras()[i].set(Parameter.USED[i])
        self.ConfigPtr = self.paras()
class J2534Lib():

    def __init__(self):
        self.Devices = dllloader.getDevices()
        self._module = sys.modules[__name__]
        self.MethodErrorLog = False
    def setDevice(self, key = 0):
        device = self.Devices[key]
        self.name = device['Name']
        self.dll = dllloader.load_dll(device['FunctionLibrary'])
        self.canlib = CanlibDll(self.dll)
    def getDevices(self):
        return self.Devices

    def SetErrorLog(self, state):
        self.MethodErrorLog = state
    def err(self, method, ret):
        if self.MethodErrorLog:
            showErr(method, ret)

    def __getattr__(self, name):
        try:
            return getattr(self.canlib, name)
        except AttributeError:
            raise AttributeError("{t} object has no attribute {n}".format(
                t=str(type(self)), n=name))
j2534lib = J2534Lib()
_err = j2534lib.err

def ptOpen():
    """Open Device
    """
    DeviceId = ct.c_ulong()
    ret = j2534lib.PassThruOpen(ct.c_void_p(None), ct.byref(DeviceId))
    _err('ptOpen',ret)
    return ret, DeviceId.value
def ptClose(DeviceId):
    """Close Device
    
    Keyword Arguments:
        DeviceId {[int]} -- Device Id Number
    """
    ret = j2534lib.PassThruClose(DeviceId)
    _err('ptClose',ret)
    return ret
def ptConnect(DeviceId, ProtocolID, Flags, BaudRate):
    """Connect

    """
    ChannelID = ct.c_ulong()
    ret = j2534lib.PassThruConnect(DeviceId, ProtocolID, Flags, BaudRate, ct.byref(ChannelID))
    _err('ptConnect',ret)
    return ret, ChannelID.value
def ptDisconnect(ChannelID):
    """ :TODO
    """
    ret = j2534lib.PassThruDisconnect(ChannelID)
    _err('ptDisconnect',ret)
    return ret
def ptReadMsgs(ChannelID, Msgs, NumMsgs, Timeout):
    """ :TODO
    """
    ret = j2534lib.PassThruReadMsgs(ChannelID, ct.byref(Msgs), ct.byref(ct.c_ulong(NumMsgs)), Timeout)
    _err('ptReadMsgs',ret)
    return ret
def ptWtiteMsgs(ChannelID, Msgs, NumMsgs, Timeout):
    """[summary]
    
    Arguments:
        ChannelID {[type]} -- [description]
        Msgs {[type]} -- [description]
        NumMsgs {[type]} -- [description]
        Timeout {[type]} -- [description]
    """
    ret = j2534lib.PassThruWriteMsgs(ChannelID, ct.byref(Msgs), ct.byref(ct.c_ulong(NumMsgs)), Timeout)
    _err('ptWtiteMsgs',ret)
    return ret
def ptStartPeriodicMsg(ChannelID, Msgs, MsgID, TimeInterval):
    """ :TODO
    """
    j2534lib.PassThruStartPeriodicMsg(ChannelID, ct.byref(Msgs), ct.byref(MsgID), TimeInterval)
def ptStopPeriodicMsg(ChannelID, MsgID):
    """ :TODO
    """
    j2534lib.PassThruStopPeriodicMsg(ChannelID, MsgID)
def ptStartMsgFilter(ChannelID, FilterType, MaskMsg, PatternMsg, FlowControlMsg):
    """ :TODO
    """
    pFilterID = ct.c_ulong()
    ret = j2534lib.PassThruStartMsgFilter(ChannelID, FilterType, ct.byref(MaskMsg), ct.byref(PatternMsg), ct.byref(FlowControlMsg), ct.byref(pFilterID))
    _err('ptStartMsgFilter',ret)
    return ret, pFilterID.value
def ptFlowControl(ChannelID, mask, pattern, flowcontrol, txflag):
    if txflag
    ptStartMsgFilter(ChannelID, FilterType.FLOW_CONTROL_FILTER, MaskMsg, PatternMsg, FlowControlMsg)
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
    ret = j2534lib.PassThruReadVersion(DeviceId, FirmwareVersion, DllVersion, ApiVersion)
    _err('ptReadVersion',ret)
    return ret, FirmwareVersion.value, DllVersion.value, ApiVersion.value
def ptGetLastError():
    """ :TODO
    """
    ErrorMsg = ct.create_string_buffer(80)
    j2534lib.PassThruGetLastError(ErrorMsg)
    return ErrorMsg.value
def ptIoctl(ChannelID, IoctlID, Input, Output):
    """ :TODO
    """
    ret = j2534lib.PassThruIoctl(ChannelID, IoctlID, Input, Output)
    _err('ptIoctl',ret)
    return ret
# IOCTL 

def GetConfig(ChannelID):
    Paras = GetParameter()
    ptIoctl(ChannelID, IoctlID.GET_CONFIG, Paras, ct.c_void_p(None))

def ReadVbat(ChannelID):
    _voltage = ct.c_ulong()
    ret = ptIoctl(ChannelID, IoctlID.READ_VBATT, ct.c_void_p(None), ct.byref(_voltage))
    return ret, _voltage.value

def ClearTxBuf(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_TX_BUFFER, ct.c_void_p(None), ct.c_void_p(None))
    return ret

def ClearRxBuf(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_RX_BUFFER, ct.c_void_p(None), ct.c_void_p(None))
    return ret