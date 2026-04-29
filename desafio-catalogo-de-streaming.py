# nomeDoFilme = input('Insira o nome do filme: ')
# anoDoFilme  = int(input('Insira o ano de lançamento do filme: '))
# notaDoFilme = float(input('Insira uma nota de 0 a 10: '))
# disponibilidadeDoFilme = bool(input('Escreva true para filme disponivel ou false para filme indisponivel: '))

# print(f'Nome do filme: {nomeDoFilme} \n',
#       f'Ano de lançamento: {anoDoFilme} \n',
#       f'nota: {notaDoFilme} \n',
#       f'Disponível: {disponibilidadeDoFilme}')



# nomeDoFilme = "Oppenheirmer"
# anoDoFilme  = 2023
# notaDoFilme = 8.4
# disponibilidadeDoFilme = True

# print("Filme: ",nomeDoFilme)
# print("Abo: ", anoDoFilme)
# print("nota: ", notaDoFilme)
# print("Disponível: ", disponibilidadeDoFilme)



#LOJA DE ROUPA
# produto1 = "Blusa"
# produto2 = "Calça"

# precoProduto1 = 50.00
# precoProduto2 = 70.00

# identificacaoProduto1 = 1
# identificacaoProduto2 = 2

# nomeCliente1 = "Sarah"
# nomeCliente2 = "João"

# idadeCliente1 = 24
# idadeCliente2 = 50

# generoCliente1 = "Feminino"
# generoCliente2 = "Masculino"


# print()
# print(f"Produtos da loja: {produto1}, {produto2}")
# print()
# print(f"Preço da Blusa: {precoProduto1:.2f}")
# print(f"Preço da calça: {precoProduto2:.2f}")
# print()
# print(f"Código de verificação da {produto1}: {identificacaoProduto1}")
# print(f"Código de verificação da {produto2}: {identificacaoProduto2}")
# print()
# print(f"Nome do cliente cadastrado: {nomeCliente1}, idade: {idadeCliente1}, gênero: {generoCliente1}")
# print()


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




