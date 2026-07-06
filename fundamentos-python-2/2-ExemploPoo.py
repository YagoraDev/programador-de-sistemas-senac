class Cliente:
    '''
    Classe para representar um cliente
    '''
    def __init__(self): #método construtor
        '''
        Inicializa um objeto da classe Cliente com atributos vazios.
        '''
        #atributos
        self.codigo = ""
        self.nome = ""
        self.telefone = ""
        #métodos de instância
    
    def cadastrar_cliente(self):
        '''
        Lógica para cadastrar o cliente
        '''
        self.codigo = input("Digite o código do cliente: ")
        self.nome = input("Digite o nome do cliente: ")
        self.telefone = input("Digite o telefone do cliente: ")
        print("Cliente cadastrado com sucesso!\n")

    def mostrar_dados(self):
        '''
        Lógica para mostrar os dados do cliente
        '''

        print(f"Código: {self.codigo}")    
        print(f"Nome: {self.nome}")    
        print(f"Telefone: {self.telefone}")

    def atualizar_cliente(self):
        '''
        Lógica para atualizar os dados do cliente
        '''
        self.codigo = input("\nDigite o novo código do cliente: ")
        self.nome = input("Digite o nome do cliente: ")
        self.telefone = input("Digite o novo telefone do cliente: ")
        print("Cliente atualizado com sucesso!")

    def excluir_cliente(self):
        '''
        Lógica para excluir o cliente
        '''
        select_cod = input("\nDigite o código do cliente que deseja excluir: ")
        if select_cod == self.codigo:
            self.codigo = ""
            self.nome = ""
            self.telefone = ""
            print("Cliente excluído com sucesso!")
        else:
            print("Código do cliente não encontrado.")

# Cliente1 precisa ser da classe cliente para utilizar os métodos da classe.
# cliente1 = Cliente() 
# cliente1.cadastrar_cliente()
# cliente1.mostrar_dados()
# cliente1.atualizar_cliente()
# cliente1.mostrar_dados()
# cliente1.excluir_cliente()
# cliente1.mostrar_dados()

# cliente2 = Cliente() 
# cliente2.cadastrar_cliente()
# cliente2.mostrar_dados()
# cliente2.atualizar_cliente()
# cliente2.mostrar_dados()
# cliente2.excluir_cliente()
# cliente2.mostrar_dados()

# cliente3 = Cliente() 
# cliente3.cadastrar_cliente()
# cliente3.mostrar_dados()
# cliente3.atualizar_cliente()
# cliente3.mostrar_dados()
# cliente3.excluir_cliente()
# cliente3.mostrar_dados()


# Lista para armazenar vários clientes
clientes = []

# Loop para cadastrar múltiplos clientes
quantidade = int(input("Quantos clientes deseja cadastrar? "))

for c in range(quantidade):
    print(f"\nCadastro do cliente {c+1}:")
    cliente = Cliente()         # Cria um novo cliente vazio
    cliente.cadastrar_cliente()
    clientes.append(cliente)    # Adiciona na lista


# Mostrar todos os clientes cadastrados
print("\n--- Lista de Clientes Cadastrados ---")
for cliente in clientes:
    cliente.mostrar_dados()