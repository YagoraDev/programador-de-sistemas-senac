# DESAFIO DO NUMERO SECRETO
numero_secreto = 8
tentativas = 0

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("Escreva um numero entre 0 a 20: "))

while number != numero_secreto:
    print("Ha ha! Você está preso no meu loop!")
    tentativas += 1
    number = int(input("Escreva um numero entre 0 a 20: "))
print(f"Muito bem, trouxa! Você está livre agora. \nTentativas: {tentativas} \nNumero secreto: {numero_secreto}")



