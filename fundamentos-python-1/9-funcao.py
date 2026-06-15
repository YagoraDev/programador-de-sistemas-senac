# FUNCAO PARA LISTAR ALUNOS MATRICULADOS EM UM CURSO
# QUASE UM CRUD

alunos = ['Ana', 'João', 'Maria', 'Pedro']

def listar_alunos():
    print(alunos)


def cadastrar_aluno():
    nome = input("Digite o nome do aluno para ser cadastrado: ")
    alunos.apend(nome)
    print(f"O aluno {nome} foi cadastrado com sucesso!")


def excluir_aluno():
    nome = input("Digite o nome do aluno a ser excluído: ")
    if nome in alunos:
        alunos.remove(nome)
        print(f"O aluno {nome} foi excluído com sucesso!")
    else:
        print("O aluno não foi exclído")


# CHAMAR A FUNCAO
# listar_alunos()
# cadastrar_aluno()
# excluir_aluno()




# FUNCAO PARA CALCULAR IDADE
def calcular_idade(ano_nascimento, ano_atual=2026):
    idade = ano_atual - ano_nascimento
    return idade

idade_ana = calcular_idade(1998)
print(f"Ana tem {idade_ana} anos.")
idade_carlos = calcular_idade(1993, 2023)
print(f"Carlos tem {idade_carlos} anos.")




# CALCULO IMC
def calcular_imc(peso,altura):
    imc = peso/altura**2
    return imc

resultado = calcular_imc(peso=70, altura=1.75)
print(f"O imc")



# FUNCAO QUE SEPARA NUMEROS MENORES DE 30 E MAIORES QUE 30 DOS VALORES QUE SAO COLOCADOS
def maior_30(*args):
    print(args)
    print(type(args))
    for num in args:
        if num > 30:
            print(f"Número maior que 30: {num}")
        else:
            print(f"Número menor que 30: {num}")
        

maior_30(40, 15, 50, 29, 71)