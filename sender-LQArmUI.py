#!/usr/bin/python3

import sys
import serial
import os
from config import config
import requests as req
params = config("settings.ini","main")
devadd = params["serial_dev_add"]
devbr = params["serial_dev_br"]
ip=params["ip"]


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
                    r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': userkom, 'log_infc': 2})

          if sys.argv[1]=="-u":
               newcmd = sys.argv[2]
               print("  Wysyłam do Arduino"+ newcmd)
               r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': newcmd, 'log_infc': 2})
               ser.write(newcmd.encode())

     else:
          newcmd = sys.argv[1]
          print("  Wysyłam do Arduino"+ newcmd)
          ## Wyślij do Arduino
          ser.write(newcmd.encode())
          r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': newcmd.encode() , 'log_infc': 0})
print("")
print("  Nie ma nic więcej do roboty...")
print("-------------------------------------------")
print("")
ser.close()
