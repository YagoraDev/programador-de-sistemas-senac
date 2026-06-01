# REMOVER ELEMENTOS DE UMA LISTA

# Qualquer um dos elementos da lista pode ser removido a qualquer momento - isso é feito com uma instrução chamada del (delete). Nota: é uma instrução, não uma função.

# Você precisa apontar para o elemento a ser removido - ele desaparecerá da lista e o comprimento da lista será reduzido em um.

numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo conteúdo da lista de originais.

numbers[0] = 111
print("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

numbers[1] = numbers[4] # Copiando o valor do quinto elemento para o segundo.
print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

print ("\nComprimento da lista:", len (numbers)) # Imprimindo comprimento de lista anterior.



del numbers[1] # Removendo o segundo elemento da lista.
print ("Comprimento da nova lista:", len (numbers)) # Imprimindo novo comprimento da lista.
print ("\nNova lista de conteúdo:", numbers) # Imprimindo conteúdo da lista atual.

