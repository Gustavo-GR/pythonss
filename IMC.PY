def inicio():
    print("Vamos realizar seu calculo de IMC")
    Peso = float(input("Digite sua Altura"))
    Altura = float(input("Digite Seu Peso "))
    resultado = Peso / (Altura * Altura)
    if(resultado <18.5):
        print(" O resultado do seu IMC é MAGREZA \n")
    elif(resultado <24.9) :
        print(" O resultado do seu IMC é NORMAL \n")
    elif(resultado <29.9):
        print(" O resultado do seu IMC é SOBREPESO \n")
    elif(resultado <34.9):
        print(" O resultado do seu IMC é OBESIDADE GRAU I \n")
    elif(resultado <39.9):
        print(" O resultado do seu IMC é OBESIDADE GRAU II \n")
    else:
        print(" O resultado do seu IMC é OBESIDADE GRAU III \n")
inicio()