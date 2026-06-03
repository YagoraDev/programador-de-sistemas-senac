'''

Dicionários em Python

Dicionários são estruturas de dados que armazenam informações na forma de pares chave: valor.

Chaves: São únicas dentro de um dicionário e geralmente são strings.
Valores: Podem ser de qualquer tipo de dado, como strings, números, listas, tuplas, outros dicionários, entre outros.

Os dicionários são definidos utilizando chaves {} e permitem acessar os valores por meio de suas respectivas chaves.

'''


# EXEMPLO DICIONARIO
pessoa = {'nome': 'Ana', 'idade': 30, 'cidade': 'belém', 'telefone': '(91)98857-8963'}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])
print(pessoa['telefone'])

# BUSCAR CHAVES, VALORES E ITENS
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa)

# BUSCAR CHAVE E VALOR COM LOOP FOR
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# ADICIONAR UM NOVO PAR CHAVE-VALOR
pessoa['Profissão'] = 'Engenheiro'
print(pessoa)

# MODIFICAR UM VALOR EXISTENTE
pessoa['Estado Civil'] = 'Solteiro'
print(pessoa) 

pessoa['notas'] = [7.0, 8.0, 9.0]
print(pessoa)

media = sum(pessoa["notas"]) / len(pessoa["notas"])
print(f"Media de notas: {media}")