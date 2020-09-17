#!/usr/bin/python3

from config import config
import serial
import psycopg2
import requests as req
params = config("settings.ini","main")
devadd = params["serial_dev_add"]
devbr = params["serial_dev_br"]

ser = serial.Serial(devadd, devbr, timeout=1)
r = req.post('http://192.168.1.13:5000/db/insert_cmd',data={'n_cmd': 'a','n_op': 'b','n_ex': 'c'})
while True:

    serBarCode = ser.readline()
    
    if len(serBarCode) >= 1:
        print(serBarCode.decode("utf-8"))


       # print(serBarCode.decode("utf-8")[len(serBarCode)-3] )
        #if serBarCode.decode("utf-8")[len(serBarCode)-3] == "a":
         
#print(r.text)
