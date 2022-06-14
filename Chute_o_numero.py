import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.TentarNovamente = True
        
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
 
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')  
               
    def Iniciar(self): 
        layout = [
            [sg.Text('Seu chute', size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))],
        ]
        self.janela = sg.Window('Chute o número!', layout=layout)
        
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while true:
                self.evento, self.valores = self.janela.Read()
                self.valor_do_chute = self.valores
            if self.evento == 'Chutar!':
                while self.TentarNovamente == True:
                    if int(self.valor_do_chute) > self.valor_aleatorio:
                        print('Chute um valor mais baixo!')
                        self.PedirValorAleatorio()
                    elif int(self.valor_do_chute) < self.valor_aleatorio:
                        print('Chute valor mais alto!')
                        self.PedirValorAleatorio()
                    if int(self.valor_do_chute) == self.valor_aleatorio:
                        self.TentarNovamente = False
                        print('Parabéns, você acertou!!!')
        except:
            print('Favor, digite apenas números!')
            self.Iniciar()
            
chute = ChuteONumero()
chute.Iniciar()