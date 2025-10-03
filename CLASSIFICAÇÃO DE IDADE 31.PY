def inicio ():
    print("OLÁ SEJA BEM VINDO A CLASSIFICAÇÃO DE IDADE \n")
    
    idade = float(input("Informe sua idade  "))
    resultado = idade
     
    print("vamos ver sua classe \n ")

    
    if resultado <= 12:
     print ("Você esta na classe Criança   \n")
    elif resultado <=17:
        print ("você esta na classe Adolecente \n")


    elif resultado <= 59:
     print ("Você esta nas pior fase, esta na classe adulto e tem conta pra pagar😑😡 \n")

   

    else:
     print ("Esta na hora de se aposentar, você esta na classe Idoso \n")


inicio()