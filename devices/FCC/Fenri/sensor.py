import modbusrtu
import ieee754

def read_ph(id):
    data = modbusrtu.read("/dev/device3",id,3,0,2)
    if data != "err":
        ph = round(ieee754.data_to_float32(data[0],data[1]),2)
        return ["ok",ph]
    else:
        return ["err",0]