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
def make_fig():
    a = int(values['-a-'])
    b = int(values['-b-'])
    f = int(values['-f-'])
    k = int(values['-k-'])
    A = int(values['-A-'])

    x = np.linspace(a,b)
    y = A * np.sin(x * f + k)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title(f"y = {A} ⋅ sin(x⋅{f}+{k})")
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    return(fig)


# =============================================================================
# Setup layout
# =============================================================================
layout = [[sg.Text('Sinusplotter: f(x) = A⋅sin(x⋅f+k) for x i [a,b]', font=("Arial", 14))],
          [sg.Text('a'), sg.Input('0', key = '-a-'), sg.Text('b'), sg.Input('10', key = '-b-')],
          [sg.Text('f'), sg.Input('1', key = '-f-'), sg.Text('k'), sg.Input('0', key = '-k-')],
          [sg.Text('A'), sg.Input('1', key = '-A-')],
          [sg.Button('lav_graf')],
          [sg.Canvas(key = '-graph-')]]

window = sg.Window('Matplotlib eksempel',
                    layout = layout,
                    finalize = True,
                    element_justification='center')

fig_gui = None

while True:
    event,values = window.read()
    print(event, values)

    if event == "lav_graf":
        if fig_gui != None:
            delete_fig(fig_gui)

        fig = make_fig()
        fig_gui = draw_figure(window['-graph-'].TKCanvas, fig)
        
    if event == sg.WIN_CLOSED:
        break

plt.close('all')
window.close()