def inicio():
    print("SEJA BEM VINDO AO facenuck!🛒✔️\n")
    senha = 89652
    tentativas = 0
    incorreta= 0
    tentativas_restantes = 3

    while tentativas < 3:
    
        incorreta = int(input("Digite sua senha "))
        tentativas += 1
        tentativas_restantes -= 1

        if incorreta != senha:
            print("SENHA INCORRETA")


        elif incorreta == senha:
            print(f"SENHA ESTA CORRETA!!, apos {tentativas} tentativas")
    print("conta bloqueada apos 3 tentativas incorreta")
inicio()
   
