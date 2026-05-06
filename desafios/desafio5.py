# SISTEMA QUE CALCULA O IMC

altura = float(input("Adicione a sua altura: "))
peso = float(input("Adicione o seu peso: "))

# PROCESSAMENTO (CALCULO IMC)
imc = (peso / (altura ** 2))

# SAIDA DE DADOS
if imc < 16:
    print(f"Seu IMC: {imc:.2f} - Baixo peso (grau 1)")
elif imc <= 16.99:
    print(f"Seu IMC: {imc:.2f} - Baixo peso (grau 2)")
elif imc <= 18.49: 
    print(f"Seu IMC: {imc:.2f} - Baixo peso (grau 3)")
elif imc <= 24.99:
    print(f"Seu IMC: {imc:.2f} - Peso adequado")
elif imc <= 29.99:
    print(f"Seu IMC: {imc:.2f} - Sobrepeso")
elif imc <= 34.99:
    print(f"Seu IMC: {imc:.2f} - Obesidade (grau 1)")
elif imc <= 39.99:
    print(f"Seu IMC: {imc:.2f} - Obesidade (grau 2)")
else:
    print(f"Seu IMC: {imc:.2f} - Obesidade (grau 3)")






