# TABUADA USANDO FOR

while True:
    num = int(input("Escolha o número da tabuada:"))
    operacao = input("Escolha a operação ( + , - , * , / ): ")
    if operacao == "+":
        print("Tabuada de Adição")
        for c in range(1,11):
            print(f"{num} + {c} = {num+c}")
    elif operacao == "-":
        print("Tabuada de Subtração")
        for c in range(1,11):
            print(f"{num} - {c} = {num-c}")
    elif operacao == "*":
        print("Tabuada da Multiplicação")
        for c in range(1,11):
            print(f"{num} x {c} = {num*c}")
    elif operacao == "/":
        print("Tabuada de Divisão")
        for c in range(1,11):
            print(f"{num} / {c} = {num/c:.1f}")
    else: print("Operador inválido")
    resposta = input("Deseja continuar? (s/n):").strip().lower()[0]
    if resposta == "n":
        break