# CAMPO DE PROVA
pessoa = {'nome': 'yago', 'idade': 20, 'cidade': 'Belém'}
print(pessoa)

pessoa["notas"] = 7.0, 8.0, 6.0
media = sum(pessoa["notas"]) / len(pessoa["notas"])
print(f"Media da pessoa: {media}")

aluno1 = {"nome": "yago", "notas": [7.0, 5.0, 9.0]}
aluno2 = {"nome": "joão", "notas": [9.0, 7.0, 8.0]}
aluno3 = {"nome": "pedro", "notas": [4.0, 8.0, 8.0]}

lista = [aluno1, aluno2, aluno3]

for aluno in lista:
    print(aluno)