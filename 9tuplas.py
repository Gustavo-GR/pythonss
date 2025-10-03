# Diferenças entre as coleções:
# - Lista: Permite elementos repetidos, mantém a ordem, e é mutável.
# - Tupla: Similar á lista, mas imútvel ( não pode ser alterada após a criação)
# - Dicionário: Armazena pares chave-valor, permitindo acesso rápido pelos nomes das chaves.
# - Conjunto: Não permite elementos duplicados e sua ordem não é garantida.



#Definição das coleções
lista= ["Ford", "Chevrolet", "Toyota", "Honda", "BMW"] # Lista: Estrutura mutável que permite elementos duplicados e pode ser alterada.
tupla= ("Ford", "Chevrolet", "Toyota", "Honda", "BMW") # Tupla: Estrutura imutável, ou seja, seus valores não podem ser alterados após a criação.
dicionario= {'sedan': "Ford", 'esportivo': "Chevrolet",'suv': "Toyota"} # Dicionário: Estrutura de chave-valor, permitindo acesso direto por chave.
conjunto = {"Ford", "Chevrolet", "Toyota", "Honda", "BMW" } # Conjunto: Estrutura que não permite elementos duplicados e não mantém ordem fixa,



# Demonstrando a mutabilidade
print("Lista antes da modificação:", lista) # Exibe a lista antes da alteração.
lista[0] = "Mercedes" # Modificando o primeiro elemento da lista, permitido pois a lista é mutável.
print("Lista após a modificação:", lista) # Exibe a lista após a alteração.

# Tentando modificar uma tupla ( isso resultará em erros se descomentado)
tupla[0] = "Mercedes" # Tuplas são imutáveis, então esta operação não é permitida.

#Acessando elementos
print("Elemento da lista índice 1:", lista[1]) # Acessa o segundo elemento da lista.
print("Elemento da tupla no índice 1:", tupla[1]) # Acessa o segundo elemento da tupla.
print("Valor da chave 'esportivo' no dicionário:", dicionario['esportivo']) # Acessa o valor associado á chave 'esportivo' no dicionário.

# Adicionando elementos
lista.append("Audi") # Adiciona "Audi" á lista.
print("Lista após adicionar elementos:", lista) # Exibe a lista após adição

dicionario['hatch'] = "Hyundai" #adiciona um novo par chave-valor ao dicionário.
print("Dicionário após adição", dicionario) # Exibe o dicionário após audição.

conjunto.add("Audi") #Adiciona "Audi" ao conjunto. Se já existir, não será adicionado novamente.
print("Conjunto após adição:", conjunto) # Exibe o conjunto após adição.

#Removendo elementos
lista.remove("Chevrolet") #Remove "Chevrolet" da lista.
print("Lista após remoção:", lista) #Exibe a lista após remoção

del dicionario['sedan'] #Remove a chave 'sedan' e seu vaalor do dicionário.
print("Dicionário após remoção:", dicionario) #Exibe o dicionário após remoção.

conjunto.discard("Toyota") # Remove " Toyota" do conjuto, se presente.
print("Conjunto após remoção:", conjunto) #Exibe o conjunto após remoção.

# Verificando a presença de elementos
print("Mercedes está na lista?", "Mercedes" in lista) # Verifica se "mercedes" está presente na lista.
print(" A chave 'suv' está no dicionário?", 'suv' in dicionario) # Verifica se a chave "suv" eiste no dicionário.
print("Honda está no conjunto?", "Honda" in conjunto) # Verifica se "Honda" está presente no conjunto.

# Convertendo entre coleções
lista_para_conjunto = set(lista) #Converte a lista para conjunto, removendo duplicatas automaticamente.
print("Lista convertida para conjunto:", lista_para_conjunto) # Exibe o conjunto gerado a partir da lista

# Iteração sobre cada estrutura
dicionario_items = [(chave, valor) for chave, valor in dicionario.items()]# Cria uma lista de tuplas contendo as chaves e valores do dicionário
print("Interando sobre dicionário:", dicionario_items) # Exibe os pares chave-valor do dicionário.

