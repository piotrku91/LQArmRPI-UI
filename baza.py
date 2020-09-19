#!/usr/bin/python3
import psycopg2
from config import config



def connect():
    
   
    try:
        
        params = config("settings.ini","postgresql")

       
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
    
    
      

def ZapytanieZrzut(Tresc,ObjektBazy):
    conn = ObjektBazy
    cur = conn.cursor()
    cur.execute(Tresc)

    print("Zapytanie: "+Tresc)
    print("Liczba zwróconych wierszy: ", cur.rowcount)
    row = cur.fetchall()
    cur.close()
    


    return row

def Zapytanie(Tresc):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(Tresc)

        print("Zapytanie: "+Tresc)
        # id = cur.fetchone()[0]
        print(conn.commit())
        cur.close()
        disconnect(conn)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return "z"
    

  #  while row is not None:
     #   print(row[1])
            
       # row = cur.fetchone()
    #cur.close()
   # disconnect(conn)
   ## return 1


