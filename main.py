import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import PySimpleGUI as sg
import time
import threading
import cv2
import random

matplotlib.use('TkAgg')

fig = matplotlib.figure.Figure(figsize=(5, 7), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(211).plot(t, np.zeros(t.shape))


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
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
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

video_capture = cv2.VideoCapture('src\\Video6.mp4')

right_column = [
    [sg.Text('Podgląd:')],
    [sg.Image(filename='', key='-CAMERA-')]
]

layout = [
    [
        sg.Column(left_column),
        sg.VSeperator(),
        sg.Column(center_column),
        sg.Column(right_column),
    ],
]

# Create the Window
window = sg.Window('Mlekołaki', layout, icon='src\\icon.ico', finalize=True)
tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)


class FlexibleThread(threading.Thread):
    def __init__(self, target, *args, **kwargs):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.running = True

    def run(self):
        while self.running:
            self.target(*self.args, **self.kwargs)

    def stop(self):
        self.running = False


def delay():
    delay = 2
    cereals[0].append(cereals[0][-1] + random.randint(0,25))
    cereals[1].append(cereals[1][-1] + random.randint(0,3))
    cereals[2].append(cereals[2][-1] + random.randint(0,25))
    cereals[3].append(cereals[3][-1] + random.randint(0,3))
    cereals[4].append(cereals[4][-1] + random.randint(0,25))
    cereals[5].append(cereals[5][-1] + random.randint(0,3))


    fig = matplotlib.figure.Figure(figsize=(5, 7), dpi=100)
    t = np.arange(0, delay * len(cereals[0]), delay)
    ax = fig.add_subplot(211)
    ax.plot(t, cereals[0],
            t, cereals[2],
            t, cereals[4])
    ax.legend(['Choco', 'Cookie', 'Corn'])

    ax = fig.add_subplot(212)

    kategorie = np.array(['Choco', 'Cookie', 'Corn'])
    wartosci_y = np.array([cereals[0][-1], cereals[2][-1], cereals[4][-1]])
    wartosci_n =  np.array([cereals[1][-1], cereals[3][-1], cereals[5][-1]])
    ax.bar(kategorie, wartosci_y, label='y')
    ax.bar(kategorie, wartosci_n, bottom=wartosci_y, label='n')
    ax.legend(['Bez defektu', 'Z defektem'])

    global tkcanvas
    tkcanvas.get_tk_widget().destroy()
    tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    time.sleep(delay)




plotUpdateThread = FlexibleThread(delay)
plotUpdateThread.start()


def showVideo():
    while (video_capture.isOpened()):
        ret, frameOrig = video_capture.read()

        if ret:
            frame = cv2.resize(frameOrig, (200, 600))
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()
            window['-CAMERA-'].update(data=imgbytes)
        else:
            break

    video_capture.release()
    videoThread.stop()


videoThread = FlexibleThread(showVideo)
videoThread.start()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

videoThread.stop()
plotUpdateThread.stop()

if video_capture.isOpened():
    video_capture.release()

cv2.destroyAllWindows()
window.close()
