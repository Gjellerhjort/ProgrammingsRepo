# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:18:26 2021

@author: Tobias Kallehauge
"""

import PySimpleGUI as sg


layout = [[sg.Text('Her er noget tekst'),],
          [sg.Input('Du kan skrive her', key = '-input-'),sg.Button('Enter')],
           [sg.Text('', key = '-output-')]]

window = sg.Window('Events', layout = layout,finalize = True)

while True:
    event,values = window.read()
    print(event, values) 
    
    if event == 'Enter':
        # print('Nogen trykkede på knappen')
        text = values['-input-']
        window['-output-'].update(text)
    
    if event == sg.WIN_CLOSED:
        break
    
    
window.close()