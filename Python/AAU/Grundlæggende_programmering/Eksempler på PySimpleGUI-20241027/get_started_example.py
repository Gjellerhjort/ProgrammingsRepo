# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:18:26 2021

@author: Tobias Kallehauge
"""

import PySimpleGUI as sg


layout = [[sg.Text('This is some text')],
          [sg.Button('This closes the window!')],
          [sg.Input('You can type here!')]]

window = sg.Window('Først vindue', layout = layout,finalize = True)

event,value = window.read()

window.close()