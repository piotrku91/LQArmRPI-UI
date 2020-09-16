import os
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def DoZwrotu(odbior):
  return ('Wyslano polecenie:<br> <textarea disabled="true" id="ok">'+odbior+'</textarea>')


@app.route('/',methods=['POST'])
def WyslijCMD():
  print ('Kliknięto przycisk.')
  text = request.form['text']
  processed_text = text.upper()
  os.system('python /home/piotr/sender.py "'+processed_text+'"')
  
  return DoZwrotu(processed_text)


@app.route('/una/')
def WyslijInne():
  print ('Odsylacz')
  processed_text='<una;>'
  os.system('python /home/piotr/sender.py "'+processed_text+'"')

  return DoZwrotu(processed_text)


if __name__ == '__main__':
  app.run(host="192.168.1.13",debug=True)

