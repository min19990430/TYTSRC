import struct


def data_to_float32(a,b):
    try:
        c = b * 65536 + a
        c_hex = "{0:#0{1}x}".format(c,10)[2:]
        #print(c_hex)
        c_float = struct.unpack('!f', bytes.fromhex(c_hex))[0]
        return c_float
    except:
        return "err"
