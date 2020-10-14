import threading
import time
import serial
import PySimpleGUI as sg
import psycopg2
import requests as req
from config import config
params = config("settings.ini","main")
devadd = params["serial_dev_add"]
devbr = params["serial_dev_br"]
ip=params["ip"]
Powitanie="** Deamon - LQ Arm UI - uruchomiony..."

try:
     ser = serial.Serial(devadd, devbr, timeout=1)
     s_on=True
except:
     s_on=False
     


THREAD_EVENT = '-THREAD-'


def the_thread(window):
    if s_on:
        window.write_event_value('-THREAD-', (Powitanie.rstrip()))
        window.TKroot.title(devadd+ " (Połączono)")
    else:
        window.write_event_value('-THREAD-', ("Nie mozna polaczyc z -"+devadd))
        window.TKroot.title(devadd+ " (Brak połączenia)")
    while s_on:
        
        time.sleep(1)
        serBarCode = ser.readline()
    
        if len(serBarCode) >= 0:
             Odczytana=serBarCode.decode("utf-8")
             window.write_event_value('-THREAD-', (Odczytana.rstrip()))
             
    if s_on: ser.close()
               # Data sent is a tuple of thread name and counter
       # window.write_event_value('-THREAD-', (threading.current_thread().name, Odczytana))      # Data sent is a tuple of thread name and counter


def main():
    sg.theme('Dark brown') 
    
    names = ['Komenda']
    
    tab1_layout = [[sg.Text('LQArmGUI Commander', font='Verdana 20')],
                  [sg.Multiline(size=(200,20), key='-ML-', disabled=True, autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True), sg.Listbox(names, size=(20, 20), enable_events=True, key='-LIST-')],
                  [sg.Input(key='-IN-',size=(190,1)),sg.B('>>',bind_return_key=True)],
                  [sg.Button('Koniec')] ]
    
    tab2_layout = [[sg.Text('Tab 2')]]
    tab3_layout = [[sg.Text('Tab 3')]]
    tab4_layout = [[sg.Text('Tab 3')]]
    
    tab_group_layout = [[sg.Tab('Konsola', tab1_layout, font='Courier 15', key='-TAB1-'),
                     sg.Tab('Tab 2', tab2_layout, visible=False, key='-TAB2-'),
                     sg.Tab('Tab 3', tab3_layout, key='-TAB3-'),
                     sg.Tab('Tab 4', tab4_layout, visible=False, key='-TAB4-'),
                     ]]



    layout = [ [sg.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-') ] ]

    window = sg.Window(devadd, layout).Finalize()
    T = threading.Thread(target=the_thread, args=(window,), daemon=True)
    T.start()
    
            
    while True:             # Event Loop
        event, values = window.read()
       # sg.cprint(event, values)
        if event == THREAD_EVENT:
            sg.cprint(f' {values[THREAD_EVENT]} ', colors='red on white')
        if event == sg.WIN_CLOSED or event == 'Exit':
               break
       
        if event.startswith('>>'):
            if s_on:
                if not values['-IN-']=="":
                     IN = '-IN-'
                     sg.cprint(f' {values[IN]} ', colors='blue on white')
                     window['-IN-'].update("")
            else:
                sg.cprint("Jesteś offline.")
                
                
    window.close()


if __name__ == '__main__':
    main()
