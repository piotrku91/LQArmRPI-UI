#!/usr/bin/python3

from config import config
import serial
import psycopg2
import requests as req
params = config("settings.ini","main")
devadd = params["serial_dev_add"]
devbr = params["serial_dev_br"]
ip=params["ip"]

ser = serial.Serial(devadd, devbr, timeout=1)

while True:

    serBarCode = ser.readline()
    
    if len(serBarCode) >= 1:
        Odczytana=serBarCode.decode("utf-8")
        print(Odczytana)
        r = req.post('http://'+ip+':5000/db/insert_logcmd',data={'log_newcmd': Odczytana, 'log_infc': 1})
       

       # print(serBarCode.decode("utf-8")[len(serBarCode)-3] )
        #if serBarCode.decode("utf-8")[len(serBarCode)-3] == "a":
         
#print(r.text)
