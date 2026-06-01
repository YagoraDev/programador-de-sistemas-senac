# Cenário

# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

# Sua tarefa:

#     escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
#     escreva uma linha de código que remova o último elemento da lista (Etapa 2)
#     escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).

# Pronto para este desafio?

hat_list = [1, 2, 3, 4, 5]

# ETAPA 1: 
hat_list[2] = int(input("Insira um número inteiro: "))
print(hat_list)

# ETAPA 2:
del hat_list[4]

# ETAPA 3: 
print("Comprimento da lista: ", len(hat_list))