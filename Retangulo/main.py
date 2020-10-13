from ClasseRetangulo import Retangulo

largura = int(input('Informe a largura do retangulo: '))
altura = int(input('Informe a altura do retangulo: '))

retangulo = Retangulo(largura, altura)

print('Escolha:')
print('1 - Para calcular a área')
print('2 - Para calcular o perímetro')
print('3 - Para saber os atributos da classe')
escolha = int(input())

if escolha == 1:
    print('Área: ', retangulo.getArea())
elif escolha == 2:
    print('Perímetro: ', retangulo.getPerimetro())
elif escolha == 3:
    retangulo.getDimension()
else:
    print('Escolha inválida, programa encerrado.')
