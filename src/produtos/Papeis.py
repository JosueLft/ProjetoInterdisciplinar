# -*- uncoding: utf-8 -*-

# Classe com o objetivo de cadastro de um produto do tipo papel

# Variaveis Globais
gramatura = 0.0
formato = ""
textura = ""
tipo = ""

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



#if __name__ == '__main__':