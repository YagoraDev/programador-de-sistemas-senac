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
frequencia = float(input("Informe a sua frequência: "))

media = (nota1 + nota2) / 2

if media >= 7 and frequencia >= 75:
    print(f"Sua média foi {media} e você foi aprovado")
elif media >= 5 and frequencia >= 75:
    print(f"Sua média foi {media} e você está de recuperação")
else:
    print(f"Sua média foi {media} e sua frequência foi {frequencia}% e você foi reprovado")
    