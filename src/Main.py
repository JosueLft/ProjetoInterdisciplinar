# -*- uncoding: utf-8 -*-

# variaveis
c = "Cadastro"
v = "Visualizar"
s = "Sair"
escolha = 0

# função
def menu():
    print("=========================")
    print("== Loft Papelaria Menu ==")
    print("=========================")
    print("  ---------------------")
    print("  ||%12s(1)  ||" % c)
    print("  ||%13s(2) ||" % v)
    print("  ||%10s(3)    ||" % s)
    print("  ---------------------")

def choosen():
    escolha = int(input("Informe o indice de sua escolha: "))
    while True:
        if(escolha == 1):
            print("\nCarregando arquivos de cadastro!")
            break
        elif(escolha == 2):
            print("\nCarregando arquivos de exibição!")
            break
        elif(escolha == 3):
            print("\nAté Logo!")
            break
        else:
            print("Opção invalida!\nPor favor informar um opção valida de acordo com os indices!")
            escolha = int(input("Informe o indice de sua escolha: "))

if __name__ == '__main__':
    menu()
    choosen()