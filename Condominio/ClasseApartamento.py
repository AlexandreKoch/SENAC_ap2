from ClasseTorre import Torre

class Apartamento:

    def __init__(self, idApartamento, numApartamento, torreApartamento):
        self.id = idApartamento
        self.num = numApartamento
        self.vaga = None
        self.torre = torreApartamento

    def getId(self):
        return self.id

    def getNum(self):
        return self.num

    def getVaga(self):
        return self.vaga

    def getTorre(self):
        return self.torre

    def setNum(self, numApartamento):
        self.num = numApartamento

    def setVaga(self, vagaApartamento):
        self.vaga = vagaApartamento

    def setTorre(self, torreApartamento):
        self.torre = torreApartamento
