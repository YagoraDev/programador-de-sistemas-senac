# SISTEMA DE CADASTRO DE ESTUDANTES
class Estudante:
    total_estudantes = 0 # atributo de classe

    def __init__(self, nome, turma, nota1, nota2):
        self.nome = nome
        self.turma = turma
        self.nota1 = nota1
        self.nota2 = nota2
        Estudante.total_estudantes += 1
    
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"{self.nome}: APROVADO (média {media:.1f})"
        else:
            return f"{self.nome}: REPROVADO (média {media:.1f})"

    def exibir_ficha(self):
        print(f"--- Ficha do estudante ---")
        print(f"Nome: {self.nome}")
        print(f"Turma: {self.turma}")
        print(f"Média: {self.calcular_media():.1f}")
        print(self.situacao())

a1 = Estudante("Carlos", "3A", 8, 9)
a2 = Estudante("Beatriz", "3A", 5, 6)

a1.exibir_ficha()
a2.exibir_ficha()
print(f"Total de estudantes cadastrados: {Estudante.total_estudantes}")