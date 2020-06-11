# -*- uncoding: utf-8 -*-

# variaveis Globais
from produtos.Produto import Produtos
arquivo = open("caixaLapis.txt", "a") # criando arquivo de texto

class CaixaLapis(Produtos):

    def __init__(self, qtd, colorido, marca, preco):
        super().__init__(marca, preco)
        self._qtd = qtd
        self._colorido = colorido

    def cadastro(self):
        lista = (super(CaixaLapis, self).cadastro(self))
        qtd = input("Informe a quantidade de lápis na caixa: ")
        cor = input("Informe se os lápis são de cor: (S/N)")

        if (cor.upper() == "S") | (cor.upper() == "SIM"):
            colorido = True
        else:
            colorido = False

        cl = CaixaLapis(qtd, colorido, lista[0], lista[1])

        caixa = (cl.marca, qtd, colorido, cl.preco)  # criando uma lista com as informações inseridas pelo usuario

        arquivo.write(str(caixa) + "\n")  # convertendo a lista para uma string e armazenando em um arquivo de texto

        print("\nCaixa de Lápis Cadastrado com Sucesso!\n")

    # get e set
    @property
    def qtd(self):
        return self._qtd

    @property
    def colorido(self):
        return self._colorido
