class Paciente:
    def __init__(self): #método construtor
        #atributos
        self.id = ""
        self.nome = ""
        self.condicao = ""
        #métodos de instância
    
    def cadastrar_paciente(self):
        # Lógica para cadastrar o cliente
        self.id = input("Digite o ID do paciente: ")
        self.nome = input("Digite o nome do paciente: ")
        self.doenca = input("Digite a condição do paciente: ")
        print("Paciente cadastrado com sucesso!\n")

    def mostrar_dados(self):
        print(f"Id: {self.id}")    
        print(f"Nome: {self.nome}")    
        print(f"Condição: {self.condicao}")

    def atualizar_paciente(self):
        # Lógica para atualizar os dados do cliente
        self.id = input("\nDigite o id do paciente: ")
        self.nome = input("Digite o nome do paciente: ")
        self.condicao = input("Digite a nova condição do paciente: ")
        print("Paciente atualizado com sucesso!")

    def excluir_paciente(self):
        # Líca para excluir o cliente
        select_id = input("\nDigite o Id do paciente que deseja excluir: ")
        if select_id == self.id:
            self.id = ""
            self.nome = ""
            self.condicao = ""
            print("Paciente excluído com sucesso!")
        else:
            print("Id do paciente não encontrado.")
    
cliente1 = Paciente() 
cliente1.cadastrar_paciente()
cliente1.mostrar_dados()
cliente1.atualizar_paciente()
cliente1.mostrar_dados()
cliente1.excluir_paciente()
cliente1.mostrar_dados()

