import random
import PySimpleGUI as sg

class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        
    layout = [
        [sg.Text('Jogar o dado?')],
        [sg.Button('sim'), sg.Button('não')],
    ]
    def Iniciar(self):
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradeçemos sua participação!')
            else:
                print('favor digitar sim ou não')
        except:
            print('Não recebi sua resposta!')
                
    def GerarValorDoDado(self):
            print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDados()
simulador.Iniciar()