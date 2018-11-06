from canlib import canlib, Frame
from canlib.canlib import ChannelData
import time

def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):
    ch = canlib.openChannel(channel, openFlags)
    print("Using channel: %s, EAN: %s" % (ChannelData(channel).device_name,
                                          ChannelData(channel).card_upc_no))
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch


def tearDownChannel(ch):
    ch.busOff()
    ch.close()

def fprint(frame):
    print('id = %s'%frame.id)
    print('id = %s'%frame.data)

print("canlib version:", canlib.dllversion())

ch0 = setUpChannel(channel=0)

frame1 = Frame(id_=0x641, data=[0x30, 0, 0, 0,0,0,0,0 ], flags=2)

time1 = time.time()

while True:
    try:
        if time.time() - time1 >20:
            break
        frame = ch0.read()
        fprint(frame)
        if frame.id == 0x241:
            ch0.write(frame1)
            
    except (canlib.canNoMsg) as ex:
        pass
    except (canlib.canError) as ex:
        print(ex)

tearDownChannel(ch0)
