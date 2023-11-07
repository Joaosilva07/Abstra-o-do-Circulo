import matplotlib.pyplot as plt

class abstracao_circulo():
    def __init__(self, raio):
        self.raio = raio
        self.x = 0
        self.y = 0
        self.calculated_area = 0
        self.calculated_perimetro = 0

    def dados_aleatorios(self):
        import random
        self.x = random.randint(0, 10000)
        self.y = random.randint(0, 10000)
        self.raio = random.randint(0, 10000)
        print("gerando dados aleatorios...")
   
    def ponto_central(self):
        print("O ponto central é: ", self.x, self.y)

    def area(self):
        self.calculated_area = round(3.14 * (self.raio ** 2), 2)
        print("A área é: ", self.calculated_area)
    
    def perimetro(self):
        self.calculated_perimetro = round(2 * 3.14 * self.raio, 2)
        print("O perímetro é: ", self.calculated_perimetro)

    def desenhar(self):
        print("Desenhando...")
        print("O raio é: ", self.raio)
        print("A coordenada x é: ", self.x)
        print("A coordenada y é: ", self.y)
        print("A área é: ", self.calculated_area)
        print("O perímetro é: ", self.calculated_perimetro)

    def grafico_desenhado(self):
        x = self.x
        y = self.y
        plt.scatter(x, y, s=self.raio*10)
        plt.show()

circulo = abstracao_circulo(3)
circulo.dados_aleatorios()
circulo.ponto_central()
circulo.area()
circulo.perimetro()
circulo.desenhar()
circulo.grafico_desenhado()