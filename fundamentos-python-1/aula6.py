# ARRAY
nomes = ["Ana", "Carlos", "Marina", "João"]

print(nomes)
print(nomes[0]) # MOSTRAR ITEM DA POSIÇÃO [0] DA LISTA
print(f"A primeira cliente cadastrada foi a {nomes[0]}")
nomes.append("Lucas") # Adicionar item no final da lista
print(nomes)
nomes[1] = "Pedro" # ADICIONAR ITEM NA POSIÇÃO 1
print(nomes)
nomes.pop(2) # APAGAR ITEM DA LISTA
print(nomes)

produtos = ["Arroz", "Feijão", "Macarrão"]
tarefas = ["Estudar Python", "Fazer exercícios", "Revisar aulas"]

produtos.append("Açucar")
tarefas.append("Ler documentação")
print("Produtos: ", produtos)
print("Tarefas: ", tarefas)
produtos.insert(2,"café") # INSERIR NO INDICE INDICADO
print(produtos)
produtos[2] = "Manteiga" # SUBSTITUI O ITEM NO INDICE [2]
print(produtos)
atividades = produtos + tarefas # CRIAR NOVA LISTA COM BASE EM OUTRAS
print("Atividades: ", atividades)
produtos.extend(tarefas) # EXTENDER UMA LISTA COM OUTRA LISTA
print("Produtos: ", tarefas)
atividades.clear() # LIMPAR TODA A LISTA
print("Lista Atividades: ", atividades)

