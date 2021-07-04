from ClasseTorre import *
from ClasseApartamento import *
from ClasseFila import *
from datetime import datetime

def carregarFila(): #monta a fila com base no arquivo txt
    arquivo = open('Fila.txt','r')
    for registro in arquivo:
        atributo = registro.split(';')
        torre = Torre(atributo[3], atributo[4], atributo[5])
        apto = Apartamento(atributo[0], atributo[1], torre)
        fila.adicionar(apto)

def imprimirTorres(): #exibe na tela as torres já cadastradas
    torres = open('Torres.txt', 'r')
    print('====================')
    print('Id - Nome - Endereço')
    print('====================')
    for linha in torres:
        atributo = linha.split(';')
        print(atributo[0], ' - ', atributo[1], ' - ', atributo[2])
    print('====================')
    torres.close()

def proximoIdTorre(): #determina o id da próxima torre que será cadastrada
    idTorre = 1
    torres = open('Torres.txt', 'r')
    for linha in torres:
        atributo = linha.split(';')
        idTorre = int(atributo[0]) + 1
    return idTorre

def validarTorre(info): #Se existir a torre, retorna o objeto, senão retorna "None"
    torres = open('Torres.txt', 'r')
    for linha in torres:
        atributo = linha.split(';')
        torre = None
        if atributo[0] == info or atributo[1] == info.upper():
            torre = Torre(atributo[0], atributo[1], atributo[2])
            return torre
        else:
            pass

def cadastrarTorre(): #cadastra uma nova torre
    print("\n")
    print("Torres cadastradas:")
    imprimirTorres()
    idTorre = proximoIdTorre()
    nomeTorre = str(input("Informe o nome da torre: "))
    while nomeTorre == "":
        nomeTorre = str(input("Informe um nome válido: "))
    enderecoTorre = str(input("Informe o endereço da torre: "))
    while enderecoTorre == "":
        enderecoTorre = str(input("Informe um endereço válido: "))
    torre = Torre(idTorre, nomeTorre, enderecoTorre)
    torre.salvar()

def salvarFila(): #salva fila com todos os dados em arquivo txt
    conteudo = []
    aux = fila.inicio
    if aux:
        arquivo = open('Fila.txt','w')
        while aux:
            novoRegistro = str(aux.apartamento.id) + ";" + str(aux.apartamento.num) + ";" + str(aux.apartamento.vaga) + ";" + str(aux.apartamento.torre.id) + ";" + str(aux.apartamento.torre.nome) + ";" + str(aux.apartamento.torre.endereco)# + "\n"
            conteudo.append(novoRegistro)
            aux = aux.proximo
        arquivo.writelines(conteudo)
        arquivo.close()

def adicionarApartamentoAFila(): #adiciona apartamento à fila e salva em txt após alteração
    print("\n")
    numApto = input("Informe o número do apartamento: ")
    torreApto =  input("Informe a torre do apartamento: ")
    torre = validarTorre(torreApto)
    while validarTorre(torreApto) == None:
        torreApto = input("Informe uma torre válida ou pressione 'Enter' para voltar: ")
        if torreApto == "":
            break
        else:
            torre = validarTorre(torreApto)
    if torreApto != "":
        idApto = str(numApto) + str(torre.getNome())
        apto = Apartamento(idApto, numApto, torre)
        fila.adicionar(apto)
        fila.imprimir()
        salvarFila()
        print("Apartamento adicionado com sucesso.")

def contemplarApartamento():
    if fila.__len__() > 0:
        #atribui uma vaga para o apartamento
        vaga = input("Informe a vaga que foi liberada: ")
        fila.inicio.apartamento.setVaga(vaga)
        #salvar no histórico
        arquivo = open('Historico.txt', 'r')
        conteudo = arquivo.readlines()
        conteudo.append(str(fila.inicio.apartamento.num) + '-' + str(fila.inicio.apartamento.torre.nome) + '-vaga ' + str(fila.inicio.apartamento.vaga) + ';\n')
        arquivo.close()
        arquivo = open('Historico.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
        #remover da fila
        fila.remover()
        salvarFila()
    else:
        print("Não há apartamentos a serem contemplados.")

def imprimirHistorico(): #exibe na tela os apartamentos já contemplados
    historico = open('Historico.txt', 'r')
    print('\n')
    print('====================')
    print('Apto - Torre - Vaga')
    print('====================')
    for linha in historico:
        print(linha)
    print('====================')
    historico.close()

print("=============== MENU ===============")
print("1- Cadastrar torre")
print("2- Adicionar apartamento à fila")
print("3- Consultar a fila")
print("4- Consultar torres cadastradas")
print("5- Consultar histórico")
print("6- Contemplar apartamento")
print("0- Finalizar")
print("====================================")

fila = Fila()
opcao = None
carregarFila()

while opcao != "0":
    opcao = input("Informe a opção desejada: ")
    if opcao == "1": #Cadastrar torre
        cadastrarTorre()
        
    elif opcao == "2": #Adicionar apartamento à fila
        adicionarApartamentoAFila()
                
    elif opcao == "3": #Consultar a fila
        fila.imprimir()
        
    elif opcao == "4": #Consultar torres cadastradas
        imprimirTorres()
        
    elif opcao == "5": #Consultar histórico
        imprimirHistorico()
        
    elif opcao == "6": #Contemplar apartamento
        contemplarApartamento()
                
    elif opcao == "0": #Finalizar
        pass
    
    else:
        opcao = input("Opção inválida, tente de novo: ")

print("Sessão finalizada com sucesso.")
