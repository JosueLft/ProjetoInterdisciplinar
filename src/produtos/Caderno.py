# -*- uncoding: utf-8 -*-

# variaveis globais
from produtos.Produto import Produtos
arquivo = open("cadenos.txt", "a")


class Caderno(Produtos):

    def __init__(self, tamanho, gramatura, qtdFolhas, capadura, nome, marca, preco):
        super().__init__(nome, marca, preco)
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
        print("\nCaderno Cadastrado com Sucesso!\n")

        if (capadura.upper() == "S") | (capadura.upper() == "SIM"):
            capa = True
        else:
            capa = False

        c = Caderno(super().nome, super().marca, super().preco, tamanho, gramatura, qtdFolhas, capa)

        caderno = (c.nome, c.marca, c.preco, tamanho, gramatura, qtdFolhas, capa)  # criando uma lista com as informações inseridas pelo usuario

        arquivo.write(str(caderno) + "\n")  # convertendo a lista para uma string e armazenando em um arquivo de texto

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