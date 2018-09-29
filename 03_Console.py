#coding:utf-8

import J2534
import argparse
from prettytable import PrettyTable

__version__ = '0.1'


def getDeviceList():
    devices = J2534.j2534lib.getDeviceList()
    table = PrettyTable( ['ID','DeviceName', 'Device Dll Path'] )
    i = 0
    for device in devices:
        table.add_row( [ i, device[0], device[1] ] )
        i = i +1
    print '\nDevices:\n'
    print table
def getDeviceVersion( id ):
    id = int(id)
    J2534.j2534lib.setDevice(id)
    deviceID = J2534.ptOpen()
    print deviceID
    firmVersion, DllVersion, ApiVersion = J2534.ptReadVersion(deviceID)
    J2534.ptClose(deviceID)
    print 'Device Version Information:\n'
    table = PrettyTable(['Firmware Version', 'Dll Version', 'Api Version'])
    table.add_row([firmVersion, DllVersion, ApiVersion])
    print table
def getDeviceConnect():
    pass
if __name__ == "__main__":
    """[summary]
        命令行解析程序，输出help文档如下所示：
        usage: use "python build.py --help" for more information

        optional arguments:
            -h, --help            show this help message and exit
            -v, --version         show program's version number and exit
    """
    parser = argparse.ArgumentParser(
        description = 'For J2534',
        version = __version__,
        usage = 'use "python %(prog)s --help" for more information!')
    parser.add_argument(
        '-D',
        '--device',
        help='Print Device List!',
        action='store_true')
    parser.add_argument(
        '-S',
        '--showVersion',
        help='Please Insert Device Id!')
    parser.add_argument(
        '-F',
        '--findDevice',
        help='Print Device current Connect!',
        action='store_true')
    parser.add_argument(
        '-T',
        '--Tx',
        help='--Tx 0')

    args = parser.parse_args()

    if args.device :
        getDeviceList()
    elif args.showVersion:
        getDeviceVersion(args.showVersion)
    elif args.findDevice:
        getDeviceConnect()