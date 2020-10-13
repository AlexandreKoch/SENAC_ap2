class Retangulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def getArea(self):
        return self.altura*self.largura
    
    def getPerimetro(self):
        return 2*self.altura + 2*self.largura

    def getDimension(self):
        return print('Largura: ', self.largura, '\nAltura: ', self.altura)