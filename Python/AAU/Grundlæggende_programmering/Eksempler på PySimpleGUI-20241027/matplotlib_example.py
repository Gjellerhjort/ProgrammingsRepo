# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:03:03 2021

@author: Tobias Kallehauge
"""

import PySimpleGUI as sg
import numpy as np
# import various funtions from matplotlib
import matplotlib 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

# =============================================================================
# Setup some helper funtioncs for plotting
# =============================================================================

def draw_figure(canvas, figure):
    """
    Draws figure on canvas for GUI
    """
    
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def delete_fig(fig):
    """
    Deletes figure from plot
    """
    fig.get_tk_widget().forget()
    plt.close('all')
    
    
# =============================================================================
# Make figure
# =============================================================================

def make_fig(n):
    x = np.linspace(-1,1)
    y = x**n
    fig, ax = plt.subplots()
    ax.plot(x,y)
    return(fig)

# =============================================================================
# Setup layout
# =============================================================================

layout = [[sg.Text('Dette er en matplotlib graf')],
          [sg.Text('Vælg n'), sg.Input('2', key = '-n-')],
           [sg.Button('Lav graf')],
           [sg.Canvas(key = '-graph-')]]


window = sg.Window('Matplotlib eksempel',
                    layout = layout,
                    finalize = True,
                    element_justification='center')

fig_gui = None

while True:
    event, values = window.read()
    
    print(event,values)
    
    if event == 'Lav graf':
        if fig_gui != None:
            delete_fig(fig_gui)
        
        n = float(values['-n-'])
        
        fig = make_fig(n)
        fig_gui = draw_figure(window['-graph-'].TKCanvas, fig)
    
    if event == sg.WIN_CLOSED:
        break
    
plt.close('all')
window.close()
    