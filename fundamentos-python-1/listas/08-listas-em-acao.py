# INVERTENDO LISTAS
variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1
 

# REVERTER A ORDEM DA LISTA
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
 
# Execute o snippet. Sua saída deve ficar assim: [5, 3, 8, 1, 10]