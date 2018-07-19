#coding:utf-8

import winreg


PASSTHRU = r"Software\\Wow6432Node\\PassThruSupport.04.04\\"
key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,PASSTHRU)
ke  = winreg.EnumKey(key, 1)
ke1  = winreg.EnumKey(key, 0)
ke2  = winreg.QueryInfoKey(key)
print (key)
print (ke)
print (ke1)
print (ke2)