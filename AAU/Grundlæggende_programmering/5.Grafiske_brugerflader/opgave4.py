import PySimpleGUI as sg

layout = [[sg.Text('Hvad er dit navn?')],
          [sg.Input('skriv dit navn her', key = '-input-'), sg.Button('Enter')],
          [sg.Text('', key = '-output-')]]

window = sg.Window('Opgave 4', layout = layout, finalize = True)

while True:
    event,values = window.read()
    print(event, values)

    if event == "Enter":
        name =  values['-input-']
        window['-output-'].update(f"{name} er et flot navn!")

    if event == sg.WIN_CLOSED:
        break

window.close()