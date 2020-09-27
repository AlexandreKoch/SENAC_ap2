from Node import Node

class LinkedList:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho
    
    def append(self, valor):
        if self.inicio:
            #quando a lista já possui valores
            aux = self.inicio
            while (aux.proximo):
                aux = aux.proximo
            aux.proximo = Node(valor)
        else:
            #quando a lista estiver vazia
            self.inicio = Node(valor)
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        if self.inicio == None:
            #se a lista estiver vazia
            print("A lista está vazia.")
        else:
            #quando a lista possui dados
            aux = self.inicio
            while (aux):
                print(aux.dado)
                aux = aux.proximo