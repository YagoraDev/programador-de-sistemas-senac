class Cliente:
    def __init__(self): #método construtor
        #atributos
        self.codigo = ""
        self.nome = ""
        self.telefone = ""
        #métodos de instância
    
    def cadastrar_cliente(self):
        # Lógica para cadastrar o cliente
        self.codigo = input("Digite o código do cliente: ")
        self.nome = input("Digite o nome do cliente: ")
        self.telefone = input("Digite o telefone do cliente: ")
        print("Cliente cadastrado com sucesso!\n")

    def mostrar_dados(self):
        print(f"Código: {self.codigo}")    
        print(f"Nome: {self.nome}")    
        print(f"Telefone: {self.telefone}")

    def atualizar_cliente(self):
        # Lógica para atualizar os dados do cliente
        self.codigo = input("\nDigite o novo código do cliente: ")
        self.nome = input("Digite o nome do cliente: ")
        self.telefone = input("Digite o novo telefone do cliente: ")
        print("Cliente atualizado com sucesso!")

    def excluir_cliente(self):
        # Líca para excluir o cliente
        select_cod = input("\nDigite o código do cliente que deseja excluir: ")
        if select_cod == self.codigo:
            self.codigo = ""
            self.nome = ""
            self.telefone = ""
            print("Cliente excluído com sucesso!")
        else:
            print("Código do cliente não encontrado.")
    
cliente1 = Cliente()
cliente1.cadastrar_cliente()
cliente1.mostrar_dados()
cliente1.atualizar_cliente()
cliente1.mostrar_dados()
cliente1.excluir_cliente()
cliente1.mostrar_dados()

