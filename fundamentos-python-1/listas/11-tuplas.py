# DESAFIO
soma = 0
contador = 0
notas = (7.5, 4.0, 6.5, 9.0, 3.5, 8.0)
for nota in notas:
    soma += nota
    if nota >= 7.0:
        contador += 1
        print(f"A nota {nota} é Aprovado")
    elif nota >= 5.0:
        print(f"A nota {nota} é Recuperação")
    else:
        print(f"A nota {nota} é Reprovado")

print(f"A média da turma é {soma/(len(notas)):.1f}")
print(f"O total de alunos aprovados é {contador}")