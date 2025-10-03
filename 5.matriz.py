import random # Importa a biblioteca random para gerar elementos aleatórios 

# Gerar matriz 3x3 com nomes de frutas 
frutas = ["Maçã, Banana", "Uva", "Laranja", "Pera", "Manga", "Abacaxi", "Melancia", "Morango"]
# Lista com nomes de frutas
matriz = [] # Cria uma lista vazia para armazenar a matriz
for i in range(3): # Loop para criar 3 linhas na matriz
    vetor = random.sample(frutas,3 ) # Seleciona aleatoriamente 3 frutas da lista
    matriz.append(vetor) # Adiciona esse vetor com uma linha na matriz

    # Exibir a matriz 
    print(" Matriz gerada com frutas:") # Mensagem para exibir a matriz

    # O i é uma variável de controle dp laço for . 
    # A função range(3) gera ps números 0, 1 e 2.
    # Assim, o laço for será executado 3 vezes, uma para cada número.
    # A cada repetção, o i assume um desses valores:
    # Primeira repetção : i = 0
    # Segunda repetção: i = 1
    # Terceira repetção: i = 2
    for linha in matriz: # Loop para percorrer cada linha da matriz
        print(linha) # Exibe cada linha da matriz

# Verificar se uma fruta está na matriz 
fruta = input("\n Digite o nome de uma fruta para buscar na matriz ")

 # Solicita uma fruta ao usuário

encontrado = False # Inciializa uma variável para verificar se a fruta foi encontrada
for i, linha in enumerate(matriz): 
    #loop para percorrer cada linha com seu índice 
    if frutas in linha: # Verifica se a fruta está na linha atual
        print(f" A fruta {fruta} está na posição: Linha {1 + 1}, coluna {linha.index(fruta) + 1} ") # Exibe a posição da fruta encontrada 
        encontrado = True # Marca que a fruta foi encontrada

        if not encontrado: # Verifica se a fruta não foi encontrada 
            print(f"A fruta {fruta} não foi encontrada na matriz" ) # A mensagem caso a fruta não seja emcontrada na matriz