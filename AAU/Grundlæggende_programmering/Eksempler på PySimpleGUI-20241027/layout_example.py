# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:57:04 2021

@author: Tobias Kallehauge
"""

import PySimpleGUI as sg


layout = [[sg.Text('This is line 1'), sg.Button('Here is a button!'), sg.Text('This is also  line1')],
          [sg.Button(f'{i}') for i in range(1,11)],
          [sg.Text('This is an input field:'), sg.Input('You can type here!')]]

window = sg.Window('Eksempel på layout', layout = layout,finalize = True)


while True:
    event,value = window.read()
