# ARRAY
from random import randint
numeros = []
for num in range(4):
    numeros.append(randint(1,10))

print(numeros)
for num in numeros:
    print("números aleatório: ", num)

for num in range(len(numeros)):
    print(f"{num+1}º número aleatório: {numeros[num]}")

print(sum(numeros))
print(f"A soma dos números: {sum(numeros)}")
print(f"O maior número: {max(numeros)}")
print(f"O menor número: {min(numeros)}")



# ESPACAMENTO ENTRE OS EXEMPLOS
print("-----------------------------------------------------------")



clientes = []
print("Informe o nome e telefone: ")
for cliente in range(2):
    clientes.append(input())

print(f"Cliente: {clientes[0]}")
print(f"Telefone: {clientes[1]}")

print("Informe o nome e telefone do segundo cliente: ")
for cliente in range(2):
    clientes.append(input())

print(f"Cliente: {clientes[0]}")
print(f"Telefone: {clientes[1]}")

Cadastro_clientes = []
Cadastro_clientes.append(clientes)
print(f"Lista Cadastro de Clientes: ", Cadastro_clientes)