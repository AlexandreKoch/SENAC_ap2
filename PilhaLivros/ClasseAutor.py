class Autor:

    def __init__(self, idAutor, nomeAutor):
        self.__id = idAutor
        self.nome = nomeAutor

    def getId(self):
        return self.__id

    def getNome(self):
        return self.nome

    def setNome(self, nomeAutor):
        self.nome = nomeAutor
