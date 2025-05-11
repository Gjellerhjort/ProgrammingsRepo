# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:20:31 2021

@author: Tobias Kallehauge
"""

import PySimpleGUI as sg
from PIL import Image
from io import BytesIO

# load banana, rezise and get raw data
banana = Image.open('banana.png')
scale = .7
scaled_size = (int(banana.size[0]*scale),int(banana.size[1]*scale))
banana = banana.resize(scaled_size)
with BytesIO() as output:
    banana.save(output, format="PNG")
    data = output.getvalue()

# =============================================================================
# Create layout and window
# =============================================================================

slider = sg.Slider((0,10), 5, orientation = 'h', enable_events=True, 
                    key ='-slider-')

table = sg.Table([['1','2'],['3','4'],['5','6'],['7','8']], headings = ('søjle 1', 'søjle 2'),
                  num_rows = 2)

check = sg.Checkbox(default = False, text =  'Banana', key = '-check-',
                      enable_events =True)

size = 300
graph = sg.Graph((size,size), graph_bottom_left= (0,0), 
                  graph_top_right=(size,size),
                  background_color = 'white',
                  key = '-graph-',
                  enable_events = True)


layout = [[slider],[table], [graph], [check]]

window = sg.Window('Eksempel på layout', layout = layout,finalize = True,
                    element_justification='center')


# =============================================================================
# Event loop
# =============================================================================

while True:
    event,values = window.read()

    print(event,values)  
    
    if event == '-graph-':
        pos = values['-graph-']
        radius = values['-slider-']
        if values['-check-']: # draw banana
            pos_img = (pos[0] - banana.size[0]/2, pos[1] + banana.size[1]/2)
            window['-graph-'].draw_image(data=data, location=pos_img)
        else:
            window['-graph-'].draw_circle(pos,radius, fill_color = 'pink')
        

    if event == sg.WIN_CLOSED:
        break
    
window.close()
    