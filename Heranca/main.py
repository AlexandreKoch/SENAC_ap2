from ClasseAluno import Aluno
from ClasseAlunoEM import AlunoEM
from ClasseAlunoGraduacao import AlunoGraduacao

grau = int(input('Digite 1 para aluno do Ensino Médio.\nDigite 2 para aluno da Graduação.\n'))

if grau == 1:
    codigo = input('Informe o código do aluno: ')
    nome = input('Informe o nome do aluno: ')
    matricula = input('Informe a matrícula do aluno: ')
    ano = input('Informe o ano do aluno: ')

    aluno = AlunoEM(codigo, nome, matricula, ano)

elif grau == 2:
    codigo = input('Informe o código do aluno: ')
    nome = input('Informe o nome do aluno: ')
    matricula = input('Informe a matrícula do aluno: ')
    semestre = input('Informe o semestre do aluno: ')

    aluno = AlunoGraduacao(codigo, nome, matricula, semestre)

else:
    print('Opção inválida, programa encerrado.')

aluno.imprime()