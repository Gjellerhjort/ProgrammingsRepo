# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:33:05 2021

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
# Setup layout - this is where you define how your window should look like
# =============================================================================

# This is just an example - each nested list is a row in the window 
# that will appear
layout = [
    [sg.Text("This is a line of some text"), sg.Button('I do nothing!')], # first row has two elements
    [[sg.Text('Here is a plot')]],
    [[sg.Canvas(key="-example plot-")]],
    [sg.Button("Exit window")],
]

# once we have our layout we can create the window
window = sg.Window(
    "PysimpleGUI example",
    layout = layout,
    finalize=True,
    element_justification="center",
)

# =============================================================================
# Here you can perform extra setup - like creating a figure
# =============================================================================

# make at test figure
fig, ax = plt.subplots()
x = np.linspace(0,10,100)
y = np.sin(x)
ax.plot(x,y)

# =============================================================================
# Here we run the events that can happen in the window
# =============================================================================


# Before we go into the loop - lets draw the figure
draw_figure(window["-example plot-"].TKCanvas, fig)


while True:
    event, values  = window.read() # wait here untill somthing happens
    print(event, values)
    # Exit the while loop when the button of close botton is pressed
    if event == "Exit window" or event == sg.WIN_CLOSED:
        break

window.close()


