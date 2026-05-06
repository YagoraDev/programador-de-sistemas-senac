# VARIAVEIS
idade = 20
salario = 5800.50
altura = 1.63
genero = "F"
nome = 'Maria Silva'



# MOSTRAR O "TIPO" DA VARIAVEL 
print(type(idade))
print(type(salario))
print(type(altura))
print(type(genero))
print(type(nome))
print('-'*80)



# VISUALIZANDO O VALOR DA VARIAVEL
print(idade) 
print('-'*80)



# UTILIZANDO STRINGS COM VARIAVEIS
print("Dados cadastrados no Sitema")
print("Nome =", nome)
print('Idade =',idade)
print("A cliente ",nome,'tem ',idade,
    'anos e sua renda mensal é de R$',salario, 'reais')
print('-'*80)



# UTILIZANDO A QUEBRA DE LINHA \n 
print("A cliente",nome, 'tem ',idade,
      'anos \ne sua renda mensal é de R$',salario, 'reais' ) 
print('-'*80)




# ARGUMENTOS
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



# SINTAXES DE SAIDA DE DADOS
print('Exemplo de print formatado')
print('A cliente {} tem {} anos e sua renda mensal é de R$ {:.2f} reais'.format(nome,idade,salario))
print()
print('-'*80)
print("A funcionaria {} tem {} do sexo {} tem {} cm e recebe {:.2f}".format(nome,idade,genero,altura,salario))
print('-'*80)



# FORMA MAIS UTILIZADA DE USAR O .format
print("Exemplo de print formatado com f strings")
print(f"A funcionaria {nome} tem {idade} do sexo {genero} tem {altura:.2f} e recebe {salario:,.2f}")
print('-'*80)

# OPERADORES ARITMETICOS
num1 = 5
num2 = 2

# SOMA
print(f"A soma de {num1} + {num2} = {num1 + num2}")
print('-'*80)

# SUBTRACAO
print(f"A Subtração de {num1} - {num2} = {num1 - num2}")
print('-'*80)

# MULTIPLICACAO
print(f"A Multiplicacao de {num1} x {num2} = {num1 ** num2}")
print('-'*80)


# DIVISAO REAL ( / ): RETORNA RESULTADOS COM CASAS DECIMAIS
print(f"A Divisão de {num1} / {num2} = {num1 / num2}")
print('-'*80)

# DIVISAO INTEIRA ( // ): RETORNA APENAS A PARTE INTEIRA DO QUOCIENTE, ARREDONDANDO PARA BAIXO(PARA MENOR INTEIRO MAIS PROXIMO).
print(f"A Divisão de numero inteiro de {num1} // {num2} = {num1 // num2}")
print('-'*80)

# Resto da divisao
print(f"O Resto da divisao de {num1} / {num2} = {num1 % num2}")
print('-'*80)

# Exponenciação
print(f"A Exponenciacao de {num1} ** {num2} = {num1} * {num2}")
print('-'*80)
