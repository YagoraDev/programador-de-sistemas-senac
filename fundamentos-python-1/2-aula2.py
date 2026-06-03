# ENTRADA DE DADOS PELO USUARIO
nome = input('Informe seu nome: ')
# SAIDA
print(f'O nome informado foi {nome}')

# APLICANDO O INPUT E PRINTANDO A VARIAVEL PARA VER O TIPO DA VARIAVEL
idade = input('Qual sua idade: ')
print(f'O usuário {nome} tem {idade} anos')
print(type(nome))
print(type(idade))

# APLICANDO A SOMA ENTRE DUAS VARIAVEIS
num1 = int(input("Informe um número"))
num2 = int(input("informe outro número"))
print(f'A soma de {num1} + {num2} = {num1 + num2}')