#coding:utf-8

def IntToID(ID):
    H4 = ID >> 24 & 0xFF
    H3 = ID >> 16 & 0xFF
    H2 = ID >> 8 & 0xFF
    H1 = ID & 0xFF
    return [ H4, H3, H2, H1 ]
def padding(size):
    '''
    1 - 7 : 7-i
    8 - n : 7 - (i-6)%7
    '''
    if size >= 1 and size <= 7:
        return 7 - size
    elif size > 7:
        return 7 - ( size - 6 )%7
