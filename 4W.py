import random #importa a biblioteca random para gerar numeros aleatorias 

# gera um número aleatoria  entre 1 e 100
numero_secreto = random.randint (1,100)

# inicializa a variavél para contar as tentativas 
tentativas = 0

# inicializa a variavél do palpite do jogador 
palpite = 0 

# exibe uma mensagem inicial para o jogador 

print("🛒 bem-vindo ao jogo de adivinhação!")
print("tente adivinhar o número entre 1 e 100")

# inicia um loop que continua até o jogador acertar o número 
while palpite != numero_secreto:
    #solicita ao usuario um número  e coverter para inteiro 
    palpite = int(input("Digite seu palpite"))
    # incrementea o contador de tentativas  
    tentativas += 1

    #verifica se o palpite é menor que o número secreto 

    if palpite < numero_secreto:
        print(" 😶muito baixo  ! tente novamente. ")
        #DA uma dica ao jogador 
        #verificar se o palpite é maior qie o número secreto 
    

        # verifica se o palpite é maior que o número secreto
    elif palpite > numero_secreto:  
        print("🛒 muito alto! tente novamante.")
        # da uma dica ao jogador 
        # sai do loop quando o palpite for igual ao número secreto 

        
print(f"😴Parabéns! você acertou o número{numero_secreto} em {tentativas} tentativas .")





