# RECEBER AS INFORMACOES DO SISTEMA DE FILMES E MOSTRAR DE FORMA ORGANIZADA

nomeDoFilme = input('Insira o nome do filme: ')
anoDoFilme  = int(input('Insira o ano de lançamento do filme: '))
notaDoFilme = float(input('Insira uma nota de 0 a 10: '))
disponibilidadeDoFilme = bool(input('Escreva true para filme disponivel ou false para filme indisponivel: '))

print(f'Nome do filme: {nomeDoFilme} \n',
      f'Ano de lançamento: {anoDoFilme} \n',
      f'nota: {notaDoFilme} \n',
      f'Disponível: {disponibilidadeDoFilme}')



nomeDoFilme = "Oppenheirmer"
anoDoFilme  = 2023
notaDoFilme = 8.4
disponibilidadeDoFilme = True

print("Filme: ",nomeDoFilme)
print("Abo: ", anoDoFilme)
print("nota: ", notaDoFilme)
print("Disponível: ", disponibilidadeDoFilme)