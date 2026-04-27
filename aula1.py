# variaveis
idade = 20
salario = 5800.50
altura = 1.63
genero = "F"
nome = 'Maria Silva'



# Mostrar o "tipo" da variavel
print(type(idade))
print(type(salario))
print(type(altura))
print(type(genero))
print(type(nome))
print('-'*80)



# Vendo o valor da variavel
print(idade) 
print('-'*80)



# Utilizando strings com variaveis
print("Dados cadastrados no Sitema")
print("Nome =", nome)
print('Idade =',idade)
print("A cliente ",nome,'tem ',idade,
    'anos e sua renda mensal é de R$',salario, 'reais')
print('-'*80)



# Utilizando a quebra de linha \n
print("A cliente",nome, 'tem ',idade,
      'anos \ne sua renda mensal é de R$',salario, 'reais' ) 
print('-'*80)




# Argumentos
print("Meu", "nome", "é", sep="_", end="*")    # sep='-' separa os espacos entre as strings com '_'.
print("Monty", "Python.", sep="*", end="*\n")  # end="*" adiciona no final do codigo o elementos selecionado e junta com o proximo print.
print('-'*80)
# Resultado: Meu_nome_é*Monty*Python.*



# Segue alguns comentários importantes
""" A funcao print é utilizada com aspas simples e duplas
# E um comentario de apenas uma linha
usar 3 aspas simples ou dupla para comentar varias linha


atalhos:
ctrl + ; comenta e descomenta
alt shift A : comentar bloco


\n quebra linha de texto
,end"" junta as linhas de outros prints
"""



# Sintaxes de saida de dados 
print('Exemplo de print formatado')
print('A cliente {} tem {} anos e sua renda mensal é de R$ {:.2f} reais'.format(nome,idade,salario))
print()
print('-'*80)
print("A funcionaria {} tem {} do sexo {} tem {} cm e recebe {:.2f}".format(nome,idade,genero,altura,salario))
print('-'*80)



# Forma mais utilizada de usar o .format
print("Exemplo de print formatado com f strings")
print(f"A funcionaria {nome} tem {idade} do sexo {genero} tem {altura:.2f} e recebe {salario:,.2f}")
print('-'*80)

# Operadores Aritmeticos
num1 = 5
num2 = 2

# Soma
print(f"A soma de {num1} + {num2} = {num1 + num2}")
print('-'*80)

# Subtracao
print(f"A Subtração de {num1} - {num2} = {num1 - num2}")
print('-'*80)

# Multiplicacao
print(f"A Multiplicacao de {num1} x {num2} = {num1 ** num2}")
print('-'*80)


# Divisao
print(f"A Divisão de {num1} / {num2} = {num1 / num2}")
print('-'*80)

# Divisao de numero inteiro
print(f"A Divisão de numero inteiro de {num1} // {num2} = {num1 // num2}")
print('-'*80)

# Resto da divisao
print(f"O Resto da divisao de {num1} / {num2} = {num1 % num2}")
print('-'*80)

# Exponenciação
print(f"A Exponenciacao de {num1} ** {num2} = {num1} * {num2}")
print('-'*80)
