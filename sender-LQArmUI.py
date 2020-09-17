#!/usr/bin/python3

import sys
import serial
import os
from config import config
params = config("settings.ini","main")
devadd = params["serial_dev_add"]
devbr = params["serial_dev_br"]


ser = serial.Serial(devadd, devbr)
os.system('clear')
print("")
print("-------------------------------------------")
print("  LQArmUI v0.2 - Moduł przekazujący")
print("  Urządzenie: "+ser.portstr)
print("-------------------------------------------")
print("  Argumenty wejściowe: "+ str(len(sys.argv)-1))
print("")
if len(sys.argv)-1>0:
     if sys.argv[1][0] == "-":
          if sys.argv[1]=="-cl":
               while True:

                    userkom = input("~ ")
                    if userkom == "exit":
                         break
                    print("  Wysyłam do Arduino "+ userkom)
          ## Wyślij do Arduino
          ser.write(userkom.encode())

     else:
          newcmd = sys.argv[1]
          print("  Wysyłam do Arduino"+ newcmd)
          ## Wyślij do Arduino
          ser.write(newcmd.encode())

print("")
print("  Nie ma nic więcej do roboty...")
print("-------------------------------------------")
print("")
ser.close()
