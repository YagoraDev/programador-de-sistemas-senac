# LOOP FOR PARA SOMAR
my_list = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list)):

  total += my_list[i]

print(total)

# Resumo:

#     1.total = 0 → variável que acumula a soma (começa em zero)
#     2.range(len(my_list)) → gera 0, 1, 2, 3, 4 (índices da lista)
#     3.total += my_list[i] → soma cada elemento: total = total + my_list[i]
#     4.print(total) → mostra 27 (10+1+8+3+5 = 27)

# Por que assim?

#     •len(my_list) = 5 → o loop roda 5 vezes
#     •my_list[0] = 10, my_list[1] = 1, etc.
#     •Usando len() o código funciona para qualquer tamanho de lista (não precisa mudar nada)

# Basta rodar o codigo. O resultado será 27.



# UTILIZANDO O SUM()
my_list = [10, 1, 8, 3, 5]
total = sum(my_list)
print(total)

