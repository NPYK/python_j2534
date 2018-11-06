#coding:utf-8
from canlib import canlib

num_channels = canlib.getNumberOfChannels()
print("Found %d channels" % num_channels)
for ch in range(0, num_channels):
    chdata = canlib.ChannelData(ch)
    print("%d. %s (%s / %s)" % (ch, chdata.device_name,
                                chdata.card_upc_no,
                                chdata.card_serial_no))
