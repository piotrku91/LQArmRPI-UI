#!/usr/bin/python3

from config import config
import serial
import psycopg2

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)


while True:

    serBarCode = ser.readline()

    if len(serBarCode) >= 1:
        print(serBarCode.decode("utf-8"))
