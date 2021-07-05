from ClasseNo import No

class Pilha:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar(self, livro):
        if self.topo:
            aux = self.topo
            self.topo = No(livro)
            self.topo.proximo = aux
        else:
            self.topo = No(livro)       
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        aux = self.topo
        while(aux):
            print(aux.livro.titulo, " - ", aux.livro.autor.nome)
            aux = aux.proximo

    def remover(self):
        if self.tamanho == 0:
            print("A pilha de livros está vazia.")
        elif self.tamanho == 1:
            self.topo = None
            self.tamanho -= 1
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
