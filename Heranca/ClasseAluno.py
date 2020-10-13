class Aluno:
    def __init__ (self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprime (self):
        print ("Código: ", self.codigo)
        print ("Nome: ", self.nome)
        print ("Matrícula: ", self.matricula)