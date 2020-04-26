# -*- uncoding: utf-8 -*-

# Classe com o objetivo de cadastro de um produto do tipo papel

# Variaveis Globais
gramatura = 0.0
formato = ""
textura = ""
tipo = ""
arquivo = open("papeis.txt", "a")

class Papel:

    def __init__(self, gramatura, formato, textura, tipo):
        self._gramatura = gramatura
        self._formato = formato
        self._textura = textura
        self._tipo = tipo

    def cad_Papel(self):
        gramatura = float(input("Informe a gramatura do papel: "))
        formato = input("Informe o formato do papel: ")
        textura = input("Informe a textura do papel: ")
        tipo = input("Informe o tipo do papel: ")
        print("\nPapel Cadastrado com Sucesso!\n")

        p = Papel(gramatura, formato, textura, tipo)

        papel = (p._gramatura, p._formato, p._textura, p._tipo, "\n")# criando uma lista com as informações inseridas pelo usuario

        arquivo.write(str(papel))# convertendo a lista para uma string e armazenando em um arquivo de texto