# OPERADORES LOGICOS (AND, OR) PARA TOMADA DE DECISAO
nome = (input("Usuario: "))
nota_prova = float(input(f"Bem vindo(a), {nome}. \ninsira a nota da prova:"))
nota_trabalho = float(input("Insira a nota do trabalho: "))

check_nota = (nota_trabalho >= 7) or (nota_prova > 7)

print()
print(f"{nome}\nAprovação: {check_nota}")



# OUTRO EXEMPLO
idade_usuario = 18
possui_carteira = True
sem_multas = True

verificador = (idade_usuario >= 18) and possui_carteira and sem_multas
print(verificador)