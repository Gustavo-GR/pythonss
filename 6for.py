soma = 0 # inicializa a variavél soma 

for i in range(30):
    numero = float (input(f"DIGITE O {i + 1}º número:"))
    if soma + numero > 30:
        print(f"⚠️  A soma não pode ultrapassar 30. {numero} não foi adicionado.")

    soma += numero 
    print(f"Soma atual: {soma}")

    if soma >= 30:
        print("✅ A soma atingiu exatamente ou proximo de  30.")
        break