"""
Solicitar a entrada do usuário dos seguintes dados: 
Nome, idade, endereco, estado_civil, escolaridade, salario1, salario2, salario3.

Processar a média salarial
Crie uma saida com todos dados informados e a média salarial
"""

nomeUsuario         = input("Digite o seu nome: ")
idadeUsuario        = input("Digite a sua idade: ")
enderecoUsuario     = input("Digite o seu endereco: ")
estadoCivilUsuario  = input("Digite o seu estado civil: ")
escolaridadeUsuario = input("Digite a sua escolaridade: ")

salario1Usuario     = float(input("Digite o seu salario 1: "))
salario2Usuario     = float(input("Digite o seu salario 2: "))
salario3Usuario     = float(input("Digite o seu salario 3: "))

media = (salario1Usuario + salario2Usuario + salario3Usuario) / 3

print(f"Nome: {nomeUsuario}")
print(f"Idade: {idadeUsuario}")
print(f"Endereço: {enderecoUsuario}")
print(f"Estado Civil: {estadoCivilUsuario}")
print(f"Escolaridade: {escolaridadeUsuario}")
print(f"Média Salarial: {media}")