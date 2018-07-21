#coding:utf-8

import sys
from dllLoader import getDeviceList, load_dll
class J2534Lib():
    def __init__(self):
        self.DeviceList = getDeviceList()
        self._module = sys.modules[__name__]
    def setDevice(self, dllPath):
        self.dll = load_dll(dllPath)
    def __getattr__(self, name):
        try:
            return getattr(self._module, name)
        except AttributeError:
            raise AttributeError("{t} object has no attribute {n}".format(
                t=str(type(self)), n=name))
    
