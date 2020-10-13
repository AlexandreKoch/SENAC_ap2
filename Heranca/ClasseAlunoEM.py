from ClasseAluno import Aluno

class AlunoEM(Aluno):
    def __init__ (self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprime (self):
        Aluno.imprime(self)
        print ("Ano: ", self.ano)