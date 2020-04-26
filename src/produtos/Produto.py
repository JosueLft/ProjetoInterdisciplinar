# -*- uncoding: utf-8 -*-

# variaveis globais


class Produtos:

    def __init__(self, nome, marca, preco):
        self._nome = nome
        self._preco = preco
        self._marca = marca

    def cadastro(self):
        nome = input("Informe o nome do produto: ")
        marca = input("Informe a marca do produto: ")
        preco = float(input("Informe o preco do Produto: "))

        return nome, preco, marca

    @property
    def nome(self):
        return self._nome

    @property
    def marca(self):
        return self._marca

    @property
    def preco(self):
        return self._preco

    @nome.setter  # metodo set
    def nome(self, nome):
            self.nome = nome