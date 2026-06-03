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

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
