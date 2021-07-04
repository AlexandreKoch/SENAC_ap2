class Torre:

    def __init__(self, idTorre, nomeTorre, enderecoTorre):
        self.id = idTorre
        self.nome = nomeTorre.upper()
        self.endereco = enderecoTorre

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getEndereco(self):
        return self.endereco

    def setNome(self, nomeTorre):
        self.nome = nomeTorre.upper()

    def setEndereco(self, enderecoTorre):
        self.endereco = enderecoTorre

    def salvar(self):
        novaLinha = str(self.id) + ';' + self.nome + ';' + self.endereco + ';\n'
        torres = open('Torres.txt', 'r')
        conteudo = torres.readlines()
        conteudo.append(novaLinha)
        torres.close()

        torres = open('Torres.txt', 'w')
        torres.writelines(conteudo)
        torres.close()
