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
  return redirect(url_for("WyslijInne",cmd=processed_text))


@app.route('/tosender/<cmd>')
def WyslijInne(cmd=None):
  print ('Odsylacz')
  processed_text=cmd
  os.system('python '+ sciezka + 'sender-LQArmUI.py "'+processed_text+'"')
  return render_template("pol.html",polecenie=processed_text)

@app.route('/db/insert',methods=['POST'])
def insert():
  tabela = request.form['tab']
  kolumny = request.form['kol']
  wartosci = request.form['val']
  a=Zapytanie('INSERT INTO '+tabela+' '+kolumny+' '+wartosci+';')
  return a

@app.route('/db/insert_cmd',methods=['POST'])
def insert_cmd():
  NewV="('"+request.form['n_cmd']+"','"+request.form['n_op']+"','"+request.form['n_ex']+"');"
  a=Zapytanie(format("INSERT INTO komendy (naglowek, opis, przyklad) VALUES {}".format(NewV)))

  return a

@app.route('/lista',methods=["GET","POST"])
def Komendy():
  db = ZapytanieZrzut('SELECT * FROM komendy ORDER BY id')
  return render_template("lista.html",db=db)


@app.route('/layout')
def laytest():
  return render_template("layout_p1.html")

if __name__ == '__main__':
  app.run(host=ip,debug=True)


