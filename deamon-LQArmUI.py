#!/usr/bin/python3

from config import config
import serial
import psycopg2
#from playsound import playsound
import requests as req
params = config("settings.ini","main")
devadd = params["serial_dev_add"]
devbr = params["serial_dev_br"]
ip=params["ip"]
Powitanie="** Deamon - LQ Arm UI - uruchomiony..."

ser = serial.Serial(devadd, devbr, timeout=1)



r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': Powitanie, 'log_infc': 0})
print(Powitanie)
while True:

    

    serBarCode = ser.readline()
    
    if len(serBarCode) >= 1:
        Odczytana=serBarCode.decode("utf-8")
        print(Odczytana)
        # playsound('wosh.wav')
        r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': Odczytana, 'log_infc': 1})

        if Odczytana.find("ar_rtn")>-1:
             part = Odczytana.split(";")
             for i in part[1:(len(part)-1)]:
                  print(i)
     

        
       

       # print(serBarCode.decode("utf-8")[len(serBarCode)-3] )
        #if serBarCode.decode("utf-8")[len(serBarCode)-3] == "a":
         
#print(r.text)
