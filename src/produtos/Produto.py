# -*- uncoding: utf-8 -*-

# variaveis globais


class Produtos:

    def __init__(self, marca, preco):
        self._preco = preco
        self._marca = marca

    def cadastro(self):
        marca = input("Informe a marca do produto: ")
        preco = float(input("Informe o preco do Produto: "))

        return preco, marca

    @property
    def marca(self):
        return self._marca

    @property
    def preco(self):
        return self._preco