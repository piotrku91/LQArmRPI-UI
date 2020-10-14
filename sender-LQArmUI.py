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
print("  LQArmUI v0.2 - Modul przekazujacy")
print("  Urzadzenie: "+ser.portstr)
print("-------------------------------------------")
print("  Argumenty wejsciowe: "+ str(len(sys.argv)-1))
print("")
if len(sys.argv)-1>0:
     if sys.argv[1][0] == "-":
          if sys.argv[1]=="-cl":
               while True:

                    userkom = input("~ ")

                    if userkom == "exit":
                         break
                    print("  Wysylam do Arduino "+ userkom)
                    ## Wyslij do Arduino
                    ser.write(userkom.encode())
                    r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': userkom, 'log_infc': 2})

          if sys.argv[1]=="-u":
               newcmd = sys.argv[2]
               print("  Wysylam do Arduino"+ newcmd)
               r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': newcmd, 'log_infc': 2})
               ser.write(newcmd.encode())

          if sys.argv[1]=="-ar":
               newcmd = sys.argv[2]
               print("  Wysylam do Arduino"+ newcmd)
               r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': newcmd, 'log_infc': 1})
               ser.write(newcmd.encode())

          if sys.argv[1]=="-ui":
               newcmd = sys.argv[2]
               print("  Wysylam do Arduino"+ newcmd)
               r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': newcmd, 'log_infc': 0})
               ser.write(newcmd.encode())

     else:
          newcmd = sys.argv[1]
          print("  Wysylam do Arduino"+ newcmd)
          ## Wyslij do Arduino
          ser.write(newcmd.encode())
          r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': newcmd.encode() , 'log_infc': 2})
print("")
print("  Nie ma nic wiecej do roboty...")
print("-------------------------------------------")
print("")
ser.close()
