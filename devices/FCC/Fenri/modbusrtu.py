import serial
import minimalmodbus
import struct
import ieee754
import time

def read(com,id,reg,start,end):
    try:
        ser = minimalmodbus.Instrument(com,id,'rtu')
        ser.serial.baudrate = 9600
        ser.serial.bytesize = 8
        ser.serial.parity = serial.PARITY_NONE
        ser.serial.stopbits = 1
        ser.serial.timeout = 2
        ser.close_port_after_each_call = True
        #ser.debug = True
        data = ser.read_registers(start ,end, functioncode = reg)
        return data
    except Exception as error:
        #print(error)
        return "err"

def write(com,id,reg,start,end):
    try:
        ser = minimalmodbus.Instrument(com,id,'rtu')
        ser.serial.baudrate = 9600
        ser.serial.bytesize = 8
        ser.serial.parity = serial.PARITY_NONE
        ser.serial.stopbits = 1
        ser.serial.timeout = 3
        ser.close_port_after_each_call = True
        #ser.debug = True
        data = ser.write_register(start ,end, functioncode = reg)
        return data
    except Exception as error:
        print(error)
        return "err"
