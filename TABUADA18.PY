# Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada de 1 a 10
print(f"\nTabuada do {numero}:")
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
