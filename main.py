import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import PySimpleGUI as sg
import time
import threading
import cv2

matplotlib.use('TkAgg')

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(211).plot(t, 2 * np.sin(2 * np.pi * t))

def draw_figure(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
   return tkcanvas
def updateLeftColumn(choco_y, choco_n, cookie_y, cookie_n, corn_y, corn_n):
    window['-CHOCO_Y-'].update(f'Brak defektu: {choco_y}')
    window['-CHOCO_N-'].update(f'Z defektem: {choco_n}')
    window['-COOKIE_Y-'].update(f'Brak defektu: {cookie_y}')
    window['-COOKIE_N-'].update(f'Z defektem: {cookie_n}')
    window['-CORN_Y-'].update(f'Brak defektu: {corn_y}')
    window['-CORN_N-'].update(f'Z defektem: {corn_n}')

sg.theme('Dark Grey 13')

choco_y = 0
choco_n = 0
cookie_y = 0
cookie_n = 0
corn_y = 0
corn_n = 0

cereals = [
    [choco_y],
    [choco_n],
    [cookie_y],
    [cookie_n],
    [corn_y],
    [corn_n],
]


left_column = [
    [sg.Text('Rodzaje płatków: ')],
    [sg.Text(f'Choco')],
    [sg.Text(f'Brak defektu: {choco_y}', key='-CHOCO_Y-')],
    [sg.Text(f'Z defektem: {choco_n}', key='-CHOCO_N-')],
    [sg.Text('Cookie')],
    [sg.Text(f'Brak defektu: {cookie_y}', key='-COOKIE_Y-')],
    [sg.Text(f'Z defektem: {cookie_n}', key='-COOKIE_N-')],
    [sg.Text('Corn')],
    [sg.Text(f'Brak defektu: {corn_y}', key='-CORN_Y-')],
    [sg.Text(f'Z defektem: {corn_n}', key='-CORN_N-')],
]

center_column = [
    [sg.Text('Wykresy:')],
    [sg.Canvas(key='-CANVAS-')],
]

right_column = [
    [sg.Text('Podgląd:')],

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
window = sg.Window('Mlekołaki', layout, icon='src\\icon.ico', finalize=True)

tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        delay = 5
        while self.running:
            time.sleep(delay)
            print('siemanko')

    def stop(self):
        self.running = False


thread = MyThread()
thread.start()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == 'Add':
        print(time.time())
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * t)
        tkcanvas.get_tk_widget().destroy()
        tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)


thread.stop()
window.close()
