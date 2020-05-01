# -*- uncoding: utf-8 -*-

# variaveis globais
from produtos.Produto import Produtos
arquivo = open("cadernos.txt", "a")


class Caderno(Produtos):

    def __init__(self, tamanho, gramatura, qtdFolhas, capadura, marca, preco):
        super().__init__(marca, preco)
        self._tamanho = tamanho
        self._gramatura = gramatura
        self._qtdFolhas = qtdFolhas
        self._capadura = capadura


    def cadastro(self):
        lista = (super(Caderno, self).cadastro(self))
        tamanho = input("Informe o tamanho do caderno: ")
        gramatura = float(input("Informe a gramatura do caderno: "))
        qtdFolhas = input("Informe a quantidade de folhas do caderno: ")
        capadura = input("Informe se é capadura o caderno: (S/N)")

        if (capadura.upper() == "S") | (capadura.upper() == "SIM"):
            capa = True
        else:
            capa = False

        c = Caderno(tamanho, gramatura, qtdFolhas, capa, lista[0], lista[1])

        caderno = (c.marca, tamanho, gramatura, qtdFolhas, capa, c.preco)  # criando uma lista com as informações inseridas pelo usuario

        arquivo.write(str(caderno) + "\n")  # convertendo a lista para uma string e armazenando em um arquivo de texto
        print("\nCaderno Cadastrado com Sucesso!\n")

    # get e set
    @property
    def gramatura(self):
        return self._gramatura

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def qtdFolhas(self):
        return self._qtdFolhas

    @property
    def capa(self):
        return self._capa