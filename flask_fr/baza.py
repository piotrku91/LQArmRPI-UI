#!/usr/bin/python3
import psycopg2
from config import config



def connect():
    
   
    try:
        
        params = config("setti","postgresql")

       
        print('Łączenie z bazą danych PostgreSQL')
        c = psycopg2.connect(**params)
				
        return c

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    
       

def disconnect(c):
    try:

        if c is not None:
            c.close()
            print('Połączenie z bazą danych zamknięte.')

      

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    
      

def listakomend():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM komendy ORDER BY id')

    print("Liczba komend :", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row[1])
            
        row = cur.fetchone()
    cur.close()
    disconnect(conn)
   ## return 1


