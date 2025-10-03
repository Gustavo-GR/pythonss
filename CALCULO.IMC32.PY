def inicio ():
    print("OLÁ SEJA BEM VINDO AO TESTE DE IMC \n")
    
    peso = float(input("Digite seu peso  "))
    altura = float(input("Digite sua altura  "))
    resultado = peso / (altura*altura)
     
    print("vamos descobrir como esta se IMC ")

    
    if resultado <= 18.5:
     print ("seu peso esta abaixo do normal  \n")
    elif resultado <=24.9:
        print ("seu peso esta normal \n")


    elif resultado <= 29.9:
     print ("seu peso esta em excesso \n")

    elif resultado <=34.4:
        print ("vc esta com obesidade classe 1 \n")


    elif resultado <=39.9:
        print ("vc esta com obesidade classe 2 \n")

    else:
     print ("vc esta com obesidade classe 3 \n")


inicio()