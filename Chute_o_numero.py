import random

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
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
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