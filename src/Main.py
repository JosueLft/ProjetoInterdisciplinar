# -*- uncoding: utf-8 -*-

# variaveis
c = "Cadastro"
v = "Visualizar"
s = "Sair"

# função
def menu():
    print("==========================")
    print("== Lofty Papelaria Menu ==")
    print("==========================\n")

    print("--------------------------")
    print("%s(1)" % c)
    print("%s(2)" % v)
    print("%s(3)" % s)
    print("--------------------------")

if __name__ == '__main__':
    menu()