#!/usr/bin/python3
import os
from flask import Flask, request, abort, redirect, url_for, render_template
from config import config
from baza import ZapytanieZrzut
from baza import Zapytanie
from baza import connect
from baza import disconnect

params = config("settings.ini","main")
sciezka=params["pathtoui"]
ip=params["ip"]
app = Flask(__name__)


@app.route('/')
def index():
  baza = connect()
  zakladki = ZapytanieZrzut('SELECT * FROM zakladkiui ORDER BY id', baza)
  naczynia_db = ZapytanieZrzut('SELECT * FROM naczynia ORDER BY id', baza)
  disconnect(baza)
  return render_template('index.html',zakladki=zakladki,naczynia_db=naczynia_db)

@app.route('/ui/action_sender',methods=['POST'])
def Triger():
  processed_text = request.form['Polecenie']
  print(processed_text);
  return redirect(url_for("WyslijInne",cmd=processed_text,u=2,esc="index"))

@app.route('/sloty')
def slots():
  baza = connect()
  zakladki = ZapytanieZrzut('SELECT * FROM zakladkiui ORDER BY id', baza)
  lq = ZapytanieZrzut('SELECT * FROM Lq_slot ORDER BY id', baza)
  disconnect(baza)
  return render_template('sloty.html',zakladki=zakladki,lq=lq)


@app.route('/konsola',methods=['POST'])
def WyslijCMD():
  print ('Kliknięto przycisk.')
  processed_text = request.form['text']
  return redirect(url_for("WyslijInne",cmd=processed_text,u=1,esc="Konsola"))


@app.route('/tosender/<cmd>/<int:u>/<esc>')
def WyslijInne(cmd=None,u=0,esc="Konsola"):
  print (u)
  processed_text=cmd
  if u==1:
    os.system('python '+ sciezka + 'sender-LQArmUI.py -u "'+processed_text+'"')
  else:
    os.system('python '+ sciezka + 'sender-LQArmUI.py -ui "'+processed_text+'"')
  return redirect(url_for(esc))

@app.route('/db/insert_cmd',methods=['POST'])
def insert_cmd():
  NewV="('"+request.form['n_cmd']+"','"+request.form['n_op']+"','"+request.form['n_ex']+"');"
  a=Zapytanie(format("INSERT INTO komendy (naglowek, opis, przyklad) VALUES {}".format(NewV)))
  return a

@app.route('/db/insert_logcmd',methods=['POST'])
def insert_logcmd():
  NewV="(NOW(),'"+request.form['log_newcmd']+"','"+request.form['log_infc']+"');"
  a=Zapytanie(format("INSERT INTO konsola (data,polecenie,interfejs) VALUES {}".format(NewV)))
  return a

@app.route('/lista',methods=["GET","POST"])
def Komendy():
  baza = connect()
  zakladki = ZapytanieZrzut('SELECT * FROM zakladkiui ORDER BY id', baza)
  db = ZapytanieZrzut('SELECT * FROM komendy ORDER BY id', baza)
  disconnect(baza)
  return render_template("lista.html",db=db,zakladki=zakladki)

@app.route('/konsola')
def Konsola():
  baza = connect()
  zakladki = ZapytanieZrzut('SELECT * FROM zakladkiui ORDER BY id', baza)
  return render_template("konsola.html",zakladki=zakladki)

@app.route('/test',methods=["GET","POST"])
def test():
  baza = connect()
  db = ZapytanieZrzut(" WITH k AS (SELECT id,to_char(data,'DD/MM HH12:MI:SS') ,polecenie, interfejs, data FROM konsola ORDER BY data DESC LIMIT 20) SELECT * FROM k ORDER BY data ASC",baza)
  disconnect(baza)
  return render_template("pol.html",db=db)


@app.route('/layout')
def laytest():
  return render_template("layout_p1.html")

if __name__ == '__main__':
  app.run(host=ip,debug=True)


