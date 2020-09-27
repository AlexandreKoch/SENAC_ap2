from LinkedList import LinkedList

listaNome = LinkedList()
listaPreco = LinkedList()
listaQuantidade = LinkedList()

def incluirProduto(nome, preco, quantidade):
    if nome and preco and quantidade:
        listaNome.append(nome)
        listaPreco.append(preco)
        listaQuantidade.append(quantidade)
        print ("Inclusão realizada com sucesso.")
    else:
        print ('Falha. É necessário informar os três parâmetros para realizar a inclusão.')

def imprimirProdutos():
    print('Nomes: ')
    listaNome.imprimir()
    print('Preços: ')
    listaPreco.imprimir()
    print('Quantidades: ')
    listaQuantidade.imprimir()



nome = str(input('Informe o nome do produto: '))
preco = input('Informe o preco do produto: ')
quantidade = input('Informe a quantidade do produto: ')

incluirProduto(nome, preco, quantidade)

print ('Número de elementos da lista: ', listaNome.__len__())

imprimirProdutos()

