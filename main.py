'''from num2words import *
from PySimpleGUI import  PySimpleGUI as sg
user = []
#layout
sg.theme('Reddit')
layout_coluna = [

    [sg.Text('NÚMERO POR EXTENSO', justification = 'center')],
    [sg.Text('digite um numero:'),sg.Input(key='numero')],
    [sg.Button('OK')],
    [sg.Text('O numero digitado é:')],
    [sg.Output(key='saida')]


]
layout = [[sg.Column(layout_coluna, element_justification='center')]]
janela = sg.Window('Número por extenso',layout)
#ler eventos
while True:
    try:
        eventos , valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'OK':
            user = num2words(valores['numero'],lang='pt_BR')
            janela.FindElement('saida').Update('')
            print(user)
    except:
        user = 'entre em contato com o administrador do programa'
        janela.FindElement('saida').Update('')
        print(user)

'''

from num2words import *
from PySimpleGUI import  PySimpleGUI as sg
user = []
#layout
sg.theme('Reddit')
layout_coluna = [
    [sg.Text('NÚMERO POR EXTENSO', font=('Arial', 11, 'bold'))],
    [sg.Text('Digite um número:', font=('Arial', 10, 'bold')), sg.Input(key='numero', size=20)],
    [sg.Button('Verificar número')],
    [sg.Text(key='')],
    [sg.Output(key='saida')]


]
layout = [[sg.Column(layout_coluna, element_justification='center')]]
janela = sg.Window('V1.0', layout)

#ler eventos
while True:
    try:
        eventos , valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Verificar número':
            user = num2words(valores['numero'],lang='pt_BR')
            print(user)
            janela.FindElement('saida').Update('')
            sg.popup(f'Número digitado foi {user}')
    except:
        user = 'entre em contato com o administrador Email:j.gabrielaraujodasilva@gmail.com'.upper()
        print(user)
        janela.FindElement('saida').Update('')
        sg.popup(f'{user}')