matriz=[]
for l in range(3):
    linha=[]
    for c in range(3):

        valor= int(input(f"digite o valor para inserir a matriz [{c}][{l}]:"))
        linha.append (valor) 
    matriz.append(linha)

    print("Matriz preenchida")
    for linha  in matriz: 
        print(linha)

