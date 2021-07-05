from ClassePilha import Pilha
from ClasseNo import No
from ClasseLivro import Livro
from ClasseAutor import Autor

pilha = Pilha()

print("1 - Incluir livro na pilha")
print("2 - Remover livro da pilha")
print("3 - Imprimir a pilha")
print("0 - Sair")

opcao = None

while opcao != "0":
    opcao = input("Informe a opção desejada: ")

    if opcao == "1":
        tituloLivro = input("Informe o título do livro: ")
        nomeAutor = input("Informe o nome do autor: ")
        idLivro = pilha.__len__() + 1001 
        idAutor = pilha.__len__() + 2001
        autor = Autor(idAutor, nomeAutor)
        livro = Livro(idLivro, tituloLivro, autor)
        pilha.adicionar(livro)
        print(pilha.topo.livro.titulo, "foi adicionado com sucesso à pilha.\n")
        #print(tituloLivro, nomeAutor, idLivro, idAutor)

    elif opcao == "2":
        print("O livro ", pilha.topo.livro.titulo, " do autor ", pilha.topo.livro.autor.nome," foi removido da pilha com sucess.")
        pilha.remover()
        print("A pilha possui ", pilha.__len__(), "livro(s).\n")
    elif opcao == "3":
        pilha.imprimir()
    elif opcao == "0":
        break
    else:
        continue
