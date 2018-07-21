import ctypes as ct

import dllLoader

class PassThru_Msg(ct.Structure):
    _fields_ = [
        ("ProtocolID", ct.c_ulong),
        ("RxStatus", ct.c_ulong),
        ("TxFlags", ct.c_ulong),
        ("Timestamp", ct.c_ulong),
        ("DataSize", ct.c_ulong),
        ("ExtraDataIndex", ct.c_ulong),
        ("Data", ct.c_char * 4128)]
class Sconfig(ct.Structure):
    _fields_ = [
        ("Parameter", ct.c_ulong),
        ("Value", ct.c_char_p)]
class Sconfig_List(ct.Structure):
    _fields_ = [
        ("NumOfParams", ct.c_ulong),
        ("BytePtr", ct.POINTER(Sconfig))]
class Sbyte_Array(ct.Structure):
    _fields_ = [
        ("NumOfBytes", ct.c_ulong),
        ("BytePtr", ct.c_char_p)]

class CanlibDll(dllLoader.MyDll):
    function_prototypes = {
        'PassThruOpen':[[ct.c_void_p, ct.POINTER(ct.c_ulong)]],
        'PassThruClose':[[ct.c_ulong]],
        'PassThruConnect':[[ct.c_ulong,ct.c_ulong,ct.c_ulong,ct.c_ulong,ct.POINTER(ct.c_ulong)]],
        'PassThruDisconnect':[[ct.c_ulong]],
        'PassThruReadMsgs':[[ct.c_ulong, ct.POINTER(PassThru_Msg), ct.POINTER(ct.c_ulong), ct.POINTER(ct.c_ulong)]],
        'PassThruWriteMsgs':[[ct.c_ulong, ct.POINTER(PassThru_Msg), ct.POINTER(ct.c_ulong), ct.POINTER(ct.c_ulong)]],
        'PassThruStartPeriodicMsg':[[ct.c_ulong, ct.POINTER(PassThru_Msg), ct.POINTER(ct.c_ulong), ct.POINTER(ct.c_ulong)]],
        'PassThruStopPeriodicMsg':[[ct.c_ulong,ct.c_ulong]],
        'PassThruStartMsgFilter':[[ct.c_ulong, ct.c_ulong, ct.POINTER(PassThru_Msg), ct.POINTER(PassThru_Msg), ct.POINTER(PassThru_Msg), ct.POINTER(ct.c_ulong)]],
        'PassThruStopMsgFilter':[[ct.c_ulong,ct.c_ulong]],
        'PassThruSetProgrammingVoltage':[[ct.c_ulong, ct.c_ulong, ct.c_ulong]],
        'PassThruReadVersion':[[ct.c_ulong, ct.c_char_p, ct.c_char_p, ct.c_char_p]],
        'PassThruGetLastError':[[ct.c_char_p]],
        'PassThruIoctl':[[ct.c_ulong,ct.c_ulong,ct.c_void_p,ct.c_void_p]]
    }

    def __init__(self, ct_dll):
        # set default values for function_prototypes
        self.default_restype = ct.c_long
        self.default_errcheck = self._error_check
        super(CanlibDll, self).__init__(ct_dll, **self.function_prototypes)

    def _error_check(self, result, func, arguments):
        """Error function used in ctype calls for canlib DLL."""
        if result < 0:
            raise print result
        else:
            return result
