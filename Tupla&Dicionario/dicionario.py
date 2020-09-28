print('Favor inserir as seguintes informações:\n')
nome = input('Nome: ')
nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))

aluno = {'nome': nome, 'primeiraNota': nota1, 'segundaNota': nota2, 'notaFinal': (nota1 + nota2)/2}

#print(aluno)
print(aluno.values())