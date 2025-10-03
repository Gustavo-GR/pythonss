def sabersobreonumero ():
    num1 = float(input("escolha o primeiro numero "))
    num2 = float(input("escolha o segundo  numero "))
     
    print("vamos descobrir quais numero esta nas classes ")

    a= num1
    b=num2
    c=a+b
    if c < 6:
     print ("é um número pequeno \n")
    elif c < 15:
       print("é um número grande \n")
    else :
       print("é um número grandão \n")
    


sabersobreonumero()