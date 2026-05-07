# VERIFICACAO DE PERMISSAO PARA DIRIGIR

ano_de_nascimento = int(input("Insira o seu ano de nascimento: "))
ano_atual = 2026
idade_atual = ano_atual - ano_de_nascimento

print(f"Você tem {idade_atual} anos")

if idade_atual < 18:
    print("Você não tem idade suficiente para dirigir.")
    anos_faltando = ano_de_nascimento + 18 - ano_atual 
    print(f"Falta {anos_faltando} anos")
elif idade_atual <= 20:
    print("Você tem idade suficiente para dirigir.")
    print("Você pode tirar a sua habilitação para carro e moto (Categorias A e B).")
else:
    print("Você tem idade suficiente para dirigir.")
    print("Você pode tirar sua habilitação para carro e moto (Categorias A e B) e habilitação profissional (Categorias C, D e E).")