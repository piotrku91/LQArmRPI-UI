#!/usr/bin/python3

import sys
import serial

#init serial port and bound
# bound rate on two ports must be the same
ser = serial.Serial('/dev/ttyACM0', 9600)
print(ser.portstr)

#send data via serial port
newcmd = sys.argv[1]
print(newcmd)
ser.write(newcmd.encode())
ser.close()
