# A lista new_list terá elementos end - start (3 - 1 = 2) - aqueles com índices iguais a 1 e 2 (mas não 3).
# O resultado do fragmento é: [8, 6]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) 


# Copiar a lista inteira.
list_1 = [1]
list_2 = list_1 [:]
list_1 [0] = 2
print (list_2)


# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)


# Com numeros negativos 
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]    # O que ficar entre o numero positivo e o numero negativo vai aparecer na nova lista.
print(new_list)             # [8, 6, 4].


# Omissao START 
my_list = [10, 8, 6, 4, 2]  
new_list = my_list[3:]      # Comeca com o START [4] e pega o restante da lista quando não tem valor definido no END.
print(new_list)             # Sua saída é, portanto: [4, 2].


# Omissao END
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]      # Comeca com END [6] e pega o restante da lista na direcao START quando não tem valor definido.
print(new_list)             # É por isso que a saída é: [10, 8, 6].


# Omissao da lista toda
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]       # Pega a lista toda.
print(new_list)             # A saída do snippet é: [10, 8, 6, 4, 2].


#----------------------------------------------------------------------------------------------------------------------------


# Instrucao del com fatiamento
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)              # O resultado do snippet é: [10, 4, 2].


# Excluir todos os elementos da lista
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)  # Lista vazia [] 


# Excluir a lista em si
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) 