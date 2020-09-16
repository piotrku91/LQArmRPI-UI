#!/usr/bin/python3

import sys
import serial
import os
from config import config

ser = serial.Serial('/dev/ttyACM0', 9600)
os.system('clear')
print("")
print("-------------------------------------------")
print("  LQArmUI v0.2 - Moduł przekazujący")
print("  Urządzenie: "+ser.portstr)
print("-------------------------------------------")
print("  Argumenty wejściowe: "+ str(len(sys.argv)-1))
print("")
if len(sys.argv)-1>0:
     newcmd = sys.argv[1]
     print("  Wysyłam do Arduino"+ newcmd)
     ## Wyślij do Arduino
     ser.write(newcmd.encode())

print("")
print("  Nie ma nic więcej do roboty...")
print("-------------------------------------------")
print("")
ser.close()
