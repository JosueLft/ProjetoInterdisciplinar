# -*- uncoding: utf-8 -*-

# variaveis globais
from Cadastro import Cadastro
from Visualizar import Visualiza

c = "Cadastro"
e = "Visualizar"
s = "Sair"
escolha = 0
p = Cadastro()
choosen = 0
v = Visualiza()

class Menu:
    # função
    def menu(self):
        print("=========================")
        print("== Loft Papelaria Menu ==")
        print("=========================")
        print("  ---------------------")
        print("  ||%12s(1)  ||" % c)
        print("  ||%13s(2) ||" % e)
        print("  ||%10s(3)    ||" % s)
        print("  ---------------------")
        m = Menu
        m.choosen(m)

    def choosen(self):
        m = Menu
        escolha = int(input("Informe o indice de sua escolha: "))
        while True:
            if(escolha == 1):
                m.cadastro(m)
                break
            elif(escolha == 2):
                m.visualiza(m)
                break
            elif(escolha == 3):
                print("\nAté Logo!")
                break
            else:
                print("Opção invalida!\nPor favor informar um opção valida de acordo com os indices!")
                escolha = int(input("Informe o indice de sua escolha: "))

    def cadastro(self):
        print("\nCarregando arquivos de cadastro!")
        p.menu_cadastro()

    def visualiza(self):
        print("\nCarregando arquivos de visualização!")
        v.menu_cadastro()

if __name__ == '__main__':
    m = Menu
    m.menu(m)