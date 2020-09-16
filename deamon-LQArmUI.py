#!/usr/bin/python3

from config import config
import serial
import psycopg2

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
    #    conn = psycopg2.connect(host="localhost",database="suppliers",user="postgres",password="Abcd1234")
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
				
        # create a cursor
        cur = conn.cursor()
        
	
        cur.execute('SELECT * FROM komendy ORDER BY id')

        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

connect()
while True:

    #read data from serial port
    serBarCode = ser.readline()

    #if there is smth do smth
    if len(serBarCode) >= 1:
        print(serBarCode.decode("utf-8"))
