#coding:utf-8

INI_RW_MSG						= 0
INI_MK_MSG						= 1
INI_PT_MSG						= 2
INI_FC_MSG						= 3
	
P_FIRMWARE_VERSION				= 0
P_DLL_VERSION					= 1
P_API_VERSION					= 2

#**************************
#* ProtocolID definitions *
#**************************
J1850VPW						= 1 # Not supported
J1850PWM				    	= 2 # Not supported
ISO9141							= 3
ISO14230						= 4
CAN							    = 5
ISO15765						= 6
SCI_A_ENGINE					= 7 # Not supported
SCI_A_TRANS						= 8 # Not supported
SCI_B_ENGINE					= 9 # Not supported
SCI_B_TRANS						= 10 # Not supported

# J2534-2 Pin Switched ProtocolIDs
J1850VPW_PS							= 0x8000 # Not supported
J1850PWM_PS							= 0x8001 # Not supported
ISO9141_PS							= 0x8002 # Not supported
ISO14230_PS							= 0x8003 # Not supported
CAN_PS								= 0x8004 # Not supported
ISO15765_PS							= 0x8005 # Not supported
J2510_PS							= 0x8006 # Not supported
SWCAN_ISO15765_PS					= 0x8007 # Not supported
SWCAN_PS							= 0x8008 # Not supported
GM_UART_PS							= 0x8009# Not supported
CAN_XON_XOFF_PS						= 0x800A# Not supported
ANALOG_IN_1							= 0x800B # Not supported
ANALOG_IN_2							= 0x800C# Not supported
ANALOG_IN_3							= 0x800D# Not supported
ANALOG_IN_4							= 0x800E# " " ...
ANALOG_IN_5							= 0x800F
ANALOG_IN_6							= 0x8010
ANALOG_IN_7							= 0x8011
ANALOG_IN_8							= 0x8012
ANALOG_IN_9							= 0x8013
ANALOG_IN_10						= 0x8014
ANALOG_IN_11						= 0x8015
ANALOG_IN_12						= 0x8016
ANALOG_IN_13						= 0x8017
ANALOG_IN_14						= 0x8018
ANALOG_IN_15						= 0x8019
ANALOG_IN_16						= 0x801A
ANALOG_IN_17						= 0x801B
ANALOG_IN_18						= 0x801C
ANALOG_IN_19						= 0x801D
ANALOG_IN_20						= 0x801E
ANALOG_IN_21						= 0x801F
ANALOG_IN_22						= 0x8020
ANALOG_IN_23						= 0x8021
ANALOG_IN_24						= 0x8022
ANALOG_IN_25						= 0x8023
ANALOG_IN_26						= 0x8024
ANALOG_IN_27						= 0x8025
ANALOG_IN_28						= 0x8026
ANALOG_IN_29						= 0x8027
ANALOG_IN_30						= 0x8028# ... " "
ANALOG_IN_31						= 0x8029# Not supported
ANALOG_IN_32						= 0x802A# Not supported

LIN_PS							= 0x10000000# Not supported
J1708_PS						= 0x10000001# Not supported

#*************/
#* IOCTL IDs */
#*************/
GET_CONFIG						= 0x01
SET_CONFIG						= 0x02
READ_VBATT						= 0x03
FIVE_BAUD_INIT					= 0x04
FAST_INIT						= 0x05
	
	
	
# unused							= 0x06
CLEAR_TX_BUFFER							= 0x07
CLEAR_RX_BUFFER							= 0x08
CLEAR_PERIODIC_MSGS						= 0x09
CLEAR_MSG_FILTERS						= 0x0A
CLEAR_FUNCT_MSG_LOOKUP_TABLE			= 0x0B # Not supported
ADD_TO_FUNCT_MSG_LOOKUP_TABLE			= 0x0C # Not supported
DELETE_FROM_FUNCT_MSG_LOOKUP_TABLE		= 0x0D # Not supported
READ_PROG_VOLTAGE						= 0x0E
	
	
	
	
# J2534-2 SWCAN
SWCAN_NS							= 0x8000 # Not supported
SWCAN_HS							= 0x8001 # Not supported
SET_POLL_RESPONSE					= 0x8002
BECOME_MASTER						= 0x8003		

# DT CarDAQ2534 Ioctl values to read most recent analog sample (Flushes all samples in queue)
READ_CH1_VOLTAGE					= 0x10000 # Not supported
READ_CH2_VOLTAGE					= 0x10001 # Not supported
READ_CH3_VOLTAGE					= 0x10002 # Not supported
READ_CH4_VOLTAGE					= 0x10003 # Not supported
READ_CH5_VOLTAGE					= 0x10004 # Not supported
READ_CH6_VOLTAGE					= 0x10005 # Not supported
	
	
	# DT CarDAQ2534 Ioctl for reading block of data
READ_ANALOG_CH1						= 0x10010 # Not supported
READ_ANALOG_CH2						= 0x10011 # Not supported
READ_ANALOG_CH3						= 0x10012 # Not supported
READ_ANALOG_CH4						= 0x10013 # Not supported
READ_ANALOG_CH5						= 0x10014 # Not supported
READ_ANALOG_CH6						= 0x10015 # Not supported
READ_TIMESTAMP						= 0x10100 # Not supported
DT_IOCTL_VVSTATS					= 0x20000000 # Not supported


#*******************************/
#* Configuration Parameter IDs */
#*******************************/
DATA_RATE							= 0x01
		
	# unused							= 0x02
LOOPBACK							=	0x03
NODE_ADDRESS						= 0x04 # Not supported
NETWORK_LINE						= 0x05 # Not supported
P1_MIN							= 0x06 # Don't use
P1_MAX							= 0x07
P2_MIN							= 0x08 # Don't use
P2_MAX							= 0x09 # Don't use
P3_MIN							= 0x0A
P3_MAX							= 0x0B # Don't use
P4_MIN							= 0x0C
P4_MAX							= 0x0D # Don't use
	
	
# See W0 = = 0x19
W1								= 0x0E
W2								= 0x0F
W3								= 0x10
W4								= 0x11
W5								= 0x12
TIDLE								= 0x13
TINIL								= 0x14
TWUP								= 0x15
PARITY							= 0x16
BIT_SAMPLE_POINT					= 0x17
SYNC_JUMP_WIDTH					= 0x18
W0								= 0x19
T1_MAX							= 0x1A
T2_MAX							= 0x1B
	
	
	
	
	# See T3_MAX							= 0x24
T4_MAX							= 0x1C
T5_MAX							= 0x1D
ISO15765_BS						= 0x1E
ISO15765_STMIN					= 0x1F
DATA_BITS							= 0x20
FIVE_BAUD_MOD						= 0x21
BS_TX								= 0x22
STMIN_TX							= 0x23
T3_MAX							= 0x24
ISO15765_WFT_MAX					= 0x25
ISO15765_SIMULTANEOUS			= 0x10000000
	
	
	# J2534-2
CAN_MIXED_FORMAT						= 0x8000
J1962_PINS							= 0x8001
SWCAN_HS_DATA_RATE					= 0x8010 # Not supported
SWCAN_SPEEDCHANGE_ENABLE				= 0x8011 # Not supported
SWCAN_RES_SWITCH						= 0x8012 # Not supported
ACTIVE_CHANNELS						= 0x8020 # Not supported
SAMPLE_RATE							= 0x8021 # Not supported
SAMPLES_PER_READING					= 0x8022 # Not supported
READINGS_PER_MSG						= 0x8023 # Not supported
AVERAGING_METHOD						= 0x8024 # Not supported
SAMPLE_RESOLUTION						= 0x8025 # Not supported
INPUT_RANGE_LOW						= 0x8026 # Not supported
INPUT_RANGE_HIGH						= 0x8027 # Not supported
	# old DT analogs
ADC_READINGS_PER_SECOND				= 0x10000 # Not supported
ADC_READINGS_PER_SAMPLE				= 0x20000 # Not supported


#*************/
#* Error IDs */
#*************/
STATUS_NOERROR						= 0x00
ERR_NOT_SUPPORTED					= 0x01
ERR_INVALID_CHANNEL_ID				= 0x02
ERR_INVALID_PROTOCOL_ID				= 0x03
ERR_NULL_PARAMETER					= 0x04
ERR_INVALID_IOCTL_VALUE				= 0x05
ERR_INVALID_FLAGS					= 0x06
ERR_FAILED							= 0x07
ERR_DEVICE_NOT_CONNECTED			= 0x08
ERR_TIMEOUT							= 0x09
ERR_INVALID_MSG						= 0x0A
ERR_INVALID_TIME_INTERVAL			= 0x0B
ERR_EXCEEDED_LIMIT					= 0x0C
ERR_INVALID_MSG_ID					= 0x0D
ERR_DEVICE_IN_USE					= 0x0E
ERR_INVALID_IOCTL_ID				= 0x0F
ERR_BUFFER_EMPTY					= 0x10
ERR_BUFFER_FULL						= 0x11
ERR_BUFFER_OVERFLOW					= 0x12
ERR_PIN_INVALID						= 0x13
ERR_CHANNEL_IN_USE					= 0x14
ERR_MSG_PROTOCOL_ID					= 0x15
ERR_INVALID_FILTER_ID				= 0x16
ERR_NO_FLOW_CONTROL					= 0x17
ERR_NOT_UNIQUE						= 0x18
ERR_INVALID_BAUDRATE				= 0x19
ERR_INVALID_DEVICE_ID				= 0x20

ERR_NULLPARAMETER					= "ERR_NULL_PARAMETER"


#*****************************/
#* Miscellaneous definitions */
#*****************************/
SHORT_TO_GROUND						= 0xFFFFFFFE # Not supported
VOLTAGE_OFF							= 0xFFFFFFFF # Not supported

NO_PARITY							= 0
ODD_PARITY							= 1
EVEN_PARITY							= 2

DISBLE_SPDCHANGE					= 0# Not supported
ENABLE_SPDCHANGE					= 1# Not supported
DISCONNECT_RESISTOR					= 0# Not supported
CONNECT_RESISTOR					= 1# Not supported
AUTO_RESISTOR						= 2# Not supported


#************************************************/
#* PassThruConnect definitions —— Connect Flag*/
#************************************************/
CAN_29BIT_ID						= 0x00000100
ISO9141_NO_CHECKSUM					= 0x00000200
CAN_ID_BOTH							= 0x00000800
ISO9141_K_LINE_ONLY					= 0x00001000
SNIFF_MODE							= 0x10000000 #DT
ISO9141_FORD_HEADER					= 0x20000000 #DT
ISO9141_NO_CHECKSUM_DT				= 0x40000000 #compat with CarDAQ2534
	#public static int CONNECT_ETHERNET_ONLY			= 0x80000000 # Not supported


#************************/
#* RxStatus definitions */
#************************/
TX_MSG_TYPE							= 0x00000001
START_OF_MESSAGE					= 0x00000002
ISO15765_FIRST_FRAME				= 0x00000002 #compat from v0202
ISO15765_EXT_ADDR					= 0x00000080 # Accidentally refered to in spec
RX_BREAK							= 0x00000004
TX_DONE								= 0x00000008
ISO15765_PADDING_ERROR				= 0x00000010
ISO15765_ADDR_TYPE					= 0x00000080
	
	
#		CAN_29BIT_ID						= 0x00000100  defined above
SWCAN_NS_RX							= 0x00040000 # Not supported
SWCAN_HS_RX							= 0x00020000 # Not supported
SWCAN_HV_RX							= 0x00010000 # Not supported


#***********************/
#* TxFlags definitions */
#***********************/
	
ISO15765_CAN_ID_29 					= 0x00000140
ISO15765_CAN_ID_11					= 0x00000040
	
#	      ISO15765_ADDR_TYPE					= 0x00000080  defined above
#		CAN_29BIT_ID						= 0x00000100  defined above
WAIT_P3_MIN_ONLY						= 0x00000200
SWCAN_HV_TX								= 0x00000400
SCI_MODE								= 0x00400000 # Not supported
SCI_TX_VOLTAGE							= 0x00800000 # Not supported


#**********************/
#* Filter definitions */
#**********************/
PASS_FILTER									= 0x00000001
BLOCK_FILTER								= 0x00000002
FLOW_CONTROL_FILTER							= 0x00000003
PASS_FILTER_WITH_TRIGGER					= 0x10000005 #DT Not Supported
BLOCK_FILTER_WITH_TRIGGER					= 0x10000006 #DT Not Supported


ISO15765_FRAME_PAD							= 0x00000040