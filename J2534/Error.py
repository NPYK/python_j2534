#coding:utf-8

# Function call successful
STATUS_NOERROR				= 0x00

# Device cannot support requested functionality mandated in this
# document. Device is not fully SAE J2534 compliant
ERR_NOT_SUPPORTED			= 0x01

# Invalid ChannelID value
ERR_INVALID_CHANNEL_ID		= 0x02

# Invalid ProtocolID value, unsupported ProtocolID, or there is a resource conflict (i.e. trying to connect to
# multiple protocols that are mutually exclusive such as J1850PWM and J1850VPW, or CAN and SCI A, etc.)
ERR_INVALID_PROTOCOL_ID		= 0x03

# NULL pointer supplied where a valid pointer is required
ERR_NULL_PARAMETER			= 0x04

# Invalid value for Ioctl parameter
ERR_INVALID_IOCTL_VALUE		= 0x05

# Invalid flag values
ERR_INVALID_FLAGS			= 0x06

# Undefined error, use PassThruGetLastError for text description
ERR_FAILED					= 0x07

# Device ID invalid
ERR_DEVICE_NOT_CONNECTED	= 0x08

# Timeout.
# PassThruReadMsg: No message available to read or could not read the specified number of
#   messages. The actual number of messages read is placed in <NumMsgs>
# PassThruWriteMsg: Device could not write the specified number of messages. The actual number of
#   messages sent on the vehicle network is placed in <NumMsgs>.
ERR_TIMEOUT					= 0x09

# Invalid message structure pointed to by pMsg (Reference Section 8 � Message Structure)
ERR_INVALID_MSG				= 0x0A

# Invalid TimeInterval value
ERR_INVALID_TIME_INTERVAL	= 0x0B

# Exceeded maximum number of message IDs or allocated space
ERR_EXCEEDED_LIMIT			= 0x0C

# Invalid MsgID value
ERR_INVALID_MSG_ID			= 0x0D

# Device is currently open
ERR_DEVICE_IN_USE			= 0x0E

# Invalid IoctlID value
ERR_INVALID_IOCTL_ID		= 0x0F

# Protocol message buffer empty, no messages available to read
ERR_BUFFER_EMPTY			= 0x10

# Protocol message buffer full. All the messages specified may not have been transmitted
ERR_BUFFER_FULL				= 0x11

# Indicates a buffer overflow occurred and messages were lost
ERR_BUFFER_OVERFLOW			= 0x12

# Invalid pin number, pin number already in use, or voltage already applied to a different pin
ERR_PIN_INVALID				= 0x13

# Channel number is currently connected
ERR_CHANNEL_IN_USE			= 0x14

# Protocol type in the message does not match the protocol associated with the Channel ID
ERR_MSG_PROTOCOL_ID			= 0x15

# Invalid Filter ID value
ERR_INVALID_FILTER_ID		= 0x16

# No flow control filter set or matched (for protocolID ISO15765 only)
ERR_NO_FLOW_CONTROL			= 0x17

# A CAN ID in pPatternMsg or pFlowControlMsg matches either ID in an existing FLOW_CONTROL_FILTER
ERR_NOT_UNIQUE				= 0x18

# The desired baud rate cannot be achieved within the tolerance specified in Section 6.5
ERR_INVALID_BAUDRATE		= 0x19

# Unable to communicate with device
ERR_INVALID_DEVICE_ID		= 0x1A