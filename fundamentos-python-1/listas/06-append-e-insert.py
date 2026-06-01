# ADICIONANDO ELEMENTOS A UMA LISTA: append() e insert()
numbers = [111, 7, 2, 1]

print(len(numbers))

print(numbers)


# APPEND()
numbers.append (4) # Ele pega o valor do argumento e o coloca no final da lista.


print(len(numbers))

print(numbers)


# INSERT()
numbers.insert (0, 222) # Ele pode adicionar um novo elemento em qualquer lugar na lista.

print(len (numbers))
print(numbers)


# UTILIZANDO LOOP COM APPEND()
my_list = [] # Criando uma lista vazia.

for i in range(5):
   my_list.append (i + 1)

print (my_list)


# UTILIZANDO LOOP COM INSERT()
my_list = []  # Criando uma lista vazia.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)
 
# OBS: O insert(0, valor) insere o elemento sempre no início da lista (índice 0).

# A cada iteração:

#     i = 0 → insere 1 na posição 0 → lista fica [1]

#     i = 1 → insere 2 na posição 0 → lista fica [2, 1]

#     i = 2 → insere 3 na posição 0 → [3, 2, 1]

#     i = 3 → insere 4 → [4, 3, 2, 1]

#     i = 4 → insere 5 → [5, 4, 3, 2, 1]

# Resultado: [5, 4, 3, 2, 1] (ordem inversa de [1, 2, 3, 4, 5]).