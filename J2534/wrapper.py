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
        """[select the device]
        
        Keyword Arguments:
            key {int} -- [the j2534 index in register ] (default: {0})
        """
        device = self.Devices[key]
        self.name = device['Name']
        self.dll = dllloader.load_dll(device['FunctionLibrary'])
        self.canlib = CanlibDll(self.dll)
    def getDevices(self):
        """[return all the devices dict]
        """
        return self.Devices

    def SetErrorLog(self, state):
        """[on / off the error log]
        
        Arguments:
            state {[bool]} -- [open or close the error log]
        """
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
    """[open selected j2534 device]
    
    Returns:
        ret  --  error type
        [type] -- [description]
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
    """Connect one channel in the J2534, if the j2534 device have more, this api will open only one.

    Returns:
        ret  --  error type
        id   --  channel id
    """
    ChannelID = ct.c_ulong()
    ret = j2534lib.PassThruConnect(DeviceId, ProtocolID, Flags, BaudRate, ct.byref(ChannelID))
    _err('ptConnect',ret)
    return ret, ChannelID.value
def ptDisconnect(ChannelID):
    """disconnect one channel
    
    Arguments:
        ChannelID {[int]} -- [description]
    
    Returns:
        [ret] -- [error type]
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
    """ TODO 
    """
    ret = j2534lib.PassThruStartPeriodicMsg(ChannelID, ct.byref(Msgs), ct.byref(MsgID), TimeInterval)
    _err('ptStartPeriodicMsg',ret)
    return ret
def ptStopPeriodicMsg(ChannelID, MsgID):
    """ stop period msg
    """
    ret = j2534lib.PassThruStopPeriodicMsg(ChannelID, MsgID)
    return ret
def ptStartMsgFilter(ChannelID, FilterType, MaskMsg, PatternMsg, FlowControlMsg):
    """ start the msg filter
    """
    pFilterID = ct.c_ulong()
    ret = j2534lib.PassThruStartMsgFilter(ChannelID, FilterType, ct.byref(MaskMsg), ct.byref(PatternMsg), ct.byref(FlowControlMsg), ct.byref(pFilterID))
    _err('ptStartMsgFilter',ret)
    return ret, pFilterID.value
def ptStopMsgFilter(ChannelID, FilterID):
    """ stop the msg filter
    """
    ret = j2534lib.PassThruStopMsgFilter(ChannelID, FilterID)
    _err('ptStopMsgFilter',ret)
    return ret
def ptSetProgrammingVoltage(DeviceID, PinNumber, Voltage):
    """ set the pin voltage
    """
    ret = j2534lib.PassThruSetProgrammingVoltage(DeviceID, PinNumber, Voltage)
    _err('ptSetProgrammingVoltage',ret)
    return ret
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
    """ get the last error
    """
    ErrorMsg = ct.create_string_buffer(80)
    j2534lib.PassThruGetLastError(ErrorMsg)
    return ErrorMsg.value
def ptIoctl(ChannelID, IoctlID, Input, Output):
    """ Ioctl base function
    """
    ret = j2534lib.PassThruIoctl(ChannelID, IoctlID, Input, Output)
    _err('ptIoctl',ret)
    return ret
# IOCTL 

def GetConfig(ChannelID, ioctlid):
    conf = SCONFIG_LIST()
    conf.NumOfParams = 1
    conf.paras = SCONFIG * 1
    conf.paras[0].setpara(ioctlid)
    conf.ConfigPtr = conf.paras()
    ret = ptIoctl(ChannelID, IoctlID.GET_CONFIG, ct.byref(conf), ct.c_void_p(None))
    return ret, conf.ConfigPtr[0].value

def SetConfig(ChannelID, ioctlid, value):
    conf = SCONFIG_LIST()
    conf.NumOfParams = 1
    conf.paras = SCONFIG * 1
    conf.paras[0].setpara(ioctlid)
    conf.paras[0].setvalue(value)
    conf.ConfigPtr = conf.paras()
    ret = ptIoctl(ChannelID, IoctlID.SET_CONFIG, ct.byref(conf), ct.c_void_p(None))
    return ret
def ReadVbat(ChannelID):
    _voltage = ct.c_ulong()
    ret = ptIoctl(ChannelID, IoctlID.READ_VBATT, ct.c_void_p(None), ct.byref(_voltage))
    return ret, _voltage.value

def ReadProgVoltage(ChannelID):
    _voltage = ct.c_ulong()
    ret = ptIoctl(ChannelID, IoctlID.READ_PROG_VOLTAGE, ct.c_void_p(None), ct.byref(_voltage))
    return ret, _voltage.value

def FiveBaudInit(ChannelID):
    return None

def FastInit(ChannelID):
    return None

def ClearTxBuf(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_TX_BUFFER, ct.c_void_p(None), ct.c_void_p(None))
    return ret

def ClearRxBuf(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_RX_BUFFER, ct.c_void_p(None), ct.c_void_p(None))
    return ret
def ClearPeriodicMsgs(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_PERIODIC_MSGS, ct.c_void_p(None), ct.c_void_p(None))
    return ret
def ClearMsgsFilters(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_MSG_FILTERS, ct.c_void_p(None), ct.c_void_p(None))
    return ret
def ClearFunctMsgLookUpTable(ChannelID):
    ret = ptIoctl(ChannelID, IoctlID.CLEAR_FUNCT_MSG_LOOKUP_TABLE, ct.c_void_p(None), ct.c_void_p(None))
    return ret
def AddToFunctMsgLookUpTable(ChannelID):
    #ret = ptIoctl(ChannelID, IoctlID.CLEAR_PERIODIC_MSGS, ct.c_void_p(None), ct.c_void_p(None))
    return None
def DeleteFromFunctMsgLookUpTable(ChannelID):
    #ret = ptIoctl(ChannelID, IoctlID.CLEAR_PERIODIC_MSGS, ct.c_void_p(None), ct.c_void_p(None))
    return None