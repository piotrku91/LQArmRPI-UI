#!/usr/bin/python3
import os
from flask import Flask, request, render_template
from config import config
from baza import listakomend

params = config("setti","main")
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
  
  os.system('python '+ sciezka + 'sender-LQArmUI.py "'+processed_text+'"')
  
  return DoZwrotu(processed_text)


@app.route('/una/')
def WyslijInne():
  print ('Odsylacz')
  processed_text='<una;>'
  os.system('python '+ sciezka + 'sender-LQArmUI.py "'+processed_text+'"')

  return DoZwrotu(processed_text)

@app.route('/komd/')
def Komendy():
  listakomend()
  return "Z"

if __name__ == '__main__':
  app.run(host=ip,debug=True)


