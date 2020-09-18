#!/usr/bin/python3
import os
from flask import Flask, request, abort, redirect, url_for, render_template
from config import config
from baza import ZapytanieZrzut
from baza import Zapytanie

params = config("settings.ini","main")
sciezka=params["pathtoui"]
ip=params["ip"]
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

def DoZwrotu(odbior):
  return ('Wyslano polecenie:<br> <textarea disabled="true" id="ok">'+odbior+'</textarea>')


@app.route('/',methods=['POST'])
def WyslijCMD():
  print ('Kliknięto przycisk.')
  processed_text = request.form['text']
  return redirect(url_for("WyslijInne",cmd=processed_text,u=1))


@app.route('/tosender/<cmd>/<int:u>')
def WyslijInne(cmd=None,u=0):
  print (u)
  processed_text=cmd
  if u==1:
    os.system('python '+ sciezka + 'sender-LQArmUI.py -u "'+processed_text+'"')
  else:
    os.system('python '+ sciezka + 'sender-LQArmUI.py "'+processed_text+'"')
  return redirect(url_for("Konsola"))

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
  db = ZapytanieZrzut('SELECT * FROM komendy ORDER BY id')
  return render_template("lista.html",db=db)

@app.route('/konsola',methods=["GET","POST"])
def Konsola():
  return render_template("konsola.html")

@app.route('/test',methods=["GET","POST"])
def test():
  db = ZapytanieZrzut(" WITH k AS (SELECT id,to_char(data,'DD/MM HH12:MI:SS') ,polecenie, interfejs, data FROM konsola ORDER BY data DESC LIMIT 20) SELECT * FROM k ORDER BY data ASC")
  return render_template("pol.html",db=db)


@app.route('/layout')
def laytest():
  return render_template("layout_p1.html")

if __name__ == '__main__':
  app.run(host=ip,debug=True)


