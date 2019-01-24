
#ProtocolID
class addBase(object):
    @staticmethod
    def value(*args):
        out = 0
        for i in args:
            out = out | i
        return out
    
    @staticmethod
    def check(flags, *args):
        for i in args:
            if flags & i:
                print (flags & i)
                pass
            else:
                return False
        return True
class ProtocolID(object):
    J1850VPW                        = 1 
    J1850PWM                        = 2 
    ISO9141                         = 3    
    ISO14230                        = 4 
    CAN                             = 5
    ISO15765                        = 6
    SCI_A_ENGINE                    = 7 
    SCI_A_TRANS                     = 8 
    SCI_B_ENGINE                    = 9 
    SCI_B_TRANS                     = 10


class Flags(addBase):
    # Flags.value(Flags.CAN_29BIT_ID,Flags.CAN_ID_BOTH)
    CAN_29BIT_ID                    = 0x00000100
    ISO9141_NO_CHECKSUM             = 0x00000200
    CAN_ID_BOTH                     = 0x00000800
    ISO9141_K_LINE_NOLY             = 0x00001000
    
class BaudRate(object):
    B500K                           = 500000
    B250K                           = 250000
class FilterType(object):
    PASS_FILTER                     = 0x00000001
    BLOCK_FILTER                    = 0x00000002
    FLOW_CONTROL_FILTER             = 0x00000003

class Voltage(object):
    SHORT_TO_GROUND =   0xFFFFFFFF
    VOLTAGE_OFF     =   0xFFFFFFFE
    @staticmethod
    def value(value):
        # Programming Voltage 
        # 0x00001388 5000mV
        # 0x00004E20 20000mV
        return value
class IoctlID(object):
    GET_CONFIG                           = 0x01
    SET_CONFIG                           = 0x02
    READ_VBATT                           = 0x03
    FIVE_BAUD_INIT                       = 0x04
    FAST_INIT                            = 0x05
    CLEAR_TX_BUFFER                      = 0x07
    CLEAR_RX_BUFFER                      = 0x08
    CLEAR_PERIODIC_MSGS                  = 0x09
    CLEAR_MSG_FILTERS                    = 0x0A
    CLEAR_FUNCT_MSG_LOOKUP_TABLE         = 0x0B # Not supported
    ADD_TO_FUNCT_MSG_LOOKUP_TABLE        = 0x0C # Not supported
    DELETE_FROM_FUNCT_MSG_LOOKUP_TABLE   = 0x0D # Not supported
    READ_PROG_VOLTAGE                    = 0x0E

class RxStatus(addBase):
    TX_MSG_TYPE                         = 0x00000001
    START_OF_MESSAGE                    = 0x00000002
    ISO15765_FIRST_FRAME                = 0x00000002 #compat from v0202
    ISO15765_EXT_ADDR                   = 0x00000080 # Accidentally refered to in spec
    RX_BREAK                            = 0x00000004
    TX_DONE                             = 0x00000008
    ISO15765_PADDING_ERROR              = 0x00000010
    ISO15765_ADDR_TYPE                  = 0x00000080
class TxFlags(addBase):
    ISO15765_CAN_ID_29                  = 0x00000140
    ISO15765_CAN_ID_11                  = 0x00000040
    ISO15765_ADDR_TYPE                  = 0x00000080  #defined above
    CAN_29BIT_ID                        = 0x00000100  #defined above
    WAIT_P3_MIN_ONLY                    = 0x00000200
    SWCAN_HV_TX                         = 0x00000400
    SCI_MODE                            = 0x00400000 # Not supported
    SCI_TX_VOLTAGE                      = 0x00800000 # Not supported
    ISO15765_FRAME_PAD                  = 0x00000040

class Parameter(object):
    
    DATA_RATE                           = 0x01
    # unused                            = 0x02
    LOOPBACK                            = 0x03
    NODE_ADDRESS                        = 0x04 # Not supported
    NETWORK_LINE                        = 0x05 # Not supported
    P1_MIN                            = 0x06 # Don't use
    P1_MAX                            = 0x07
    P2_MIN                            = 0x08 # Don't use
    P2_MAX                            = 0x09 # Don't use
    P3_MIN                            = 0x0A
    P3_MAX                            = 0x0B # Don't use
    P4_MIN                            = 0x0C
    P4_MAX                            = 0x0D # Don't use
    # See W0 = = 0x19
    W1                                = 0x0E
    W2                                = 0x0F
    W3                                = 0x10
    W4                                = 0x11
    W5                                = 0x12
    TIDLE                             = 0x13
    TINIL                             = 0x14
    TWUP                              = 0x15
    PARITY                            = 0x16
    class PARITY_ENUM(object):
        NO_PARITY                     = 0
        ODD_PARITY                    = 1
        EVEN_PARITY                   = 2
    BIT_SAMPLE_POINT                  = 0x17
    SYNC_JUMP_WIDTH                   = 0x18
    W0                                = 0x19
    T1_MAX                            = 0x1A
    T2_MAX                            = 0x1B
    T3_MAX                            = 0x24
    T4_MAX                            = 0x1C
    T5_MAX                            = 0x1D
    ISO15765_BS                       = 0x1E
    ISO15765_STMIN                    = 0x1F
    DATA_BITS                         = 0x20
    FIVE_BAUD_MOD                     = 0x21
    BS_TX                             = 0x22
    STMIN_TX                          = 0x23
    T3_MAX                            = 0x24
    ISO15765_WFT_MAX                  = 0x25
    USED = [
        DATA_RATE,LOOPBACK,NODE_ADDRESS,NETWORK_LINE,P1_MAX,P3_MIN,P4_MIN,\
        W0,W1,W2,W3,W4,W5,TIDLE,TINIL,TWUP,PARITY,BIT_SAMPLE_POINT,SYNC_JUMP_WIDTH,\
        T1_MAX,T2_MAX,T3_MAX,T4_MAX,T5_MAX,\
        ISO15765_BS,ISO15765_STMIN,DATA_BITS,FIVE_BAUD_MOD,BS_TX,STMIN_TX,T3_MAX,ISO15765_WFT_MAX
    ]