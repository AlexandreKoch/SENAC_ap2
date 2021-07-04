from ClasseNo import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho

    def adicionar(self, apartamento):
        if self.inicio:
            aux = self.inicio
            while (aux.proximo):
                aux = aux.proximo
            aux.proximo = No(apartamento)
        else:
            self.inicio = No(apartamento)
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        aux = None
        aux = self.inicio
        if (aux):
            print("\nSegue a fila de espera por vagas:")
            while(aux):
                print(str(aux.apartamento.getNum()) + ' - ' + str(aux.apartamento.torre.nome))
                aux = aux.proximo
        else:
            print("Não há fila de espera por vagas.")
        print("\n")

    def remover(self):
        if self.tamanho == 0:
            print("Não há apartamentos na fila.")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            if self.tamanho == 0:
                print("A fila foi zerada.")

