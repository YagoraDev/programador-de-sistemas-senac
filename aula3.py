# CONDICIONAL
# ESTRUTURA DE CONTROLE CONDICOES ANINHADAS IF ELIF ELSE

idade = 18
if idade > 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# CONDICAO PARA APROVACAO
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 7):
    print("Parabens você passou de ano!")
else:
    print("Infelizmente você não atingiu a média")