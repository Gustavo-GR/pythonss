import random

numero_secreto = random.randint(1, 100)
tentativas = 0
palpite = 0

print("🛒 Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100")

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("😶 Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("🛒 Muito alto! Tente novamente.")

print(f"😴 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
