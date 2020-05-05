# -*- uncoding: utf-8 -*-

# variaveis globais
tabela = []

class Produtos:

    def __init__(self, marca, preco):
        self._preco = preco
        self._marca = marca

    def cadastro(self):
        marca = input("Informe a marca do produto: ")
        preco = float(input("Informe o preco do Produto: "))

        return preco, marca

    def visualiza(self, arquivo):
        arquivo = arquivo + ".txt"
        file = open(arquivo, "r")

        for linha in file:  # for utilizado para ler linha a linha do arquivo de texto
            linha = linha.strip()
            tabela.append(linha)

        #tabela.insert(0, [i[0], i[1], i[2], i[3], i[4], i[5]])

        for i in tabela:
            print(i)
        file.close()

    @property
    def marca(self):
        return self._marca

    @property
    def preco(self):
        return self._preco