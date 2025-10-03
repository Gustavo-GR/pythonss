soma = 0  # Inicializa a variável de soma

contador = 1
while contador <= 5:
    numero = float(input(f"Digite o {contador}º número: "))
    soma += numero
    contador += 1

print(f"\nA soma total dos números é: {soma}")
