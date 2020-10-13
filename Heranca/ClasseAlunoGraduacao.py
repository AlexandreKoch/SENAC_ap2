from ClasseAluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__ (self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprime (self):
        Aluno.imprime(self)
        print ("Semestre: ", self.semestre)