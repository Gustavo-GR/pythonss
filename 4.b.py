def inicio():
    print("SEJA BEM VINDO AO BANCO DO POVO!🛍️\n")
    senha = 1001 
    tentativas = 0
    incorreta= 0

    while incorreta != senha:
    
        incorreta = int(input("Digite sua senha "))
        tentativas += 1

        if incorreta != senha:
            print("SENHA INCORRETA")


        elif incorreta == senha:
            print(f"SENHA ESTA CORRETA!!, apos {tentativas} tentativas")

inicio()
   
