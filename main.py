import PySimpleGUI as sg

sg.theme('Dark Grey 13')

choco_y = 0
choco_n = 0
cookie_y = 0
cookie_n = 0
corn_y = 0
corn_n = 0

left_column = [
    [sg.Text(f'Choco:')],
    [sg.Text(f'Brak defektu: {choco_y}', key='-CHOCO_Y-')],
    [sg.Text(f'Z defektem: {choco_n}', key='-CHOCO_N-')],
    [sg.Text('Cookie: ')],
    [sg.Text(f'Brak defektu: {cookie_y}', key='-COOKIE_Y-')],
    [sg.Text(f'Z defektem: {cookie_n}', key='-COOKIE_N-')],
    [sg.Text('Corn: ')],
    [sg.Text(f'Brak defektu: {corn_y}', key='-CORN_Y-')],
    [sg.Text(f'Z defektem: {corn_n}', key='-CORN_N-')],
]

center_column = [
    [sg.Text('Choco: ')],
    [sg.Text('Brak defektu: ')],
    [sg.Text('Z defektem: ')],
    [sg.Text('Cookie: ')],
    [sg.Text('Brak defektu: ')],
    [sg.Text('Z defektem: ')],
    [sg.Text('Corn: ')],
    [sg.Text('Brak defektu: ')],
    [sg.Text('Z defektem: ')],
]

right_column = [
    [sg.Text('Choco: ')],
    [sg.Text('Brak defektu: ')],
    [sg.Text('Z defektem: ')],
    [sg.Text('Cookie: ')],
    [sg.Text('Brak defektu: ')],
    [sg.Text('Z defektem: ')],
    [sg.Text('Corn: ')],
    [sg.Text('Brak defektu: ')],
    [sg.Text('Z defektem: ')],
]

# All the stuff inside your window.
layout = [
    [
        sg.Column(left_column),
        sg.VSeperator(),
        sg.Column(center_column),
        sg.VSeperator(),
        sg.Column(right_column),
    ],
    [sg.Button('Add')]
]

# Create the Window
window = sg.Window('Mlekołaki', layout, icon='src\\icon.ico')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == 'Add':
        choco_y += 1
        choco_n += 2
        cookie_y += 3
        cookie_n += 4
        corn_y += 5
        corn_n += 6
        window['-CHOCO_Y-'].update(f'Brak defektu: {choco_y}')
        window['-CHOCO_N-'].update(f'Z defektem: {choco_n}')
        window['-COOKIE_Y-'].update(f'Brak defektu: {cookie_y}')
        window['-COOKIE_N-'].update(f'Z defektem: {cookie_n}')
        window['-CORN_Y-'].update(f'Brak defektu: {corn_y}')
        window['-CORN_N-'].update(f'Z defektem: {corn_n}')

window.close()
