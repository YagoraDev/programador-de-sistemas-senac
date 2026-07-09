# Exemplo 2 - posicionamento absoluto com 
# place() - define a posição do widget

import tkinter as tk
janela = tk.Tk()
janela.title("Exemplo 2 - Place")
janela.geometry("800x600")


rotulo1 = tk.Label(janela, text="CADASTRO DE CLIENTES",font=("Arial", 20))
rotulo1.pack(pady=10)

# CAMPO NOME
rotulo_nome = tk.Label(janela, text="Nome: ", font=("Arial", 12))
rotulo_nome.place(x=50, y=100)

caixa_nome = tk.Entry(janela, font=("Arial", 12))
caixa_nome.place(x=130, y=100, width=400, height=30)


# CAMPO CPF
rotulo_cpf = tk.Label(janela, text="Cpf: ", font=("Arial", 12))
rotulo_cpf.place(x=50, y=150)

caixa_cpf = tk.Entry(janela, font=("Arial", 12))
caixa_cpf.place(x=130, y=150, width=400, height=30)


#CAMPO ENDEREÇO
rotulo_endereco = tk.Label(janela, text="Endereço: ", font=("Arial", 12))
rotulo_endereco.place(x=50, y=200)

caixa_endereco = tk.Entry(janela, font=("Arial", 12))
caixa_endereco.place(x=130, y=200, width=400, height=30)





botao1 = tk.Button(
    janela, 
    text="SALVAR", 
    bg="#325834",
    fg="#ffffff", 
    font=("Arial", 12)
)
botao1.place(x=20, y=500, width=200, height=50)

botao2 = tk.Button(
    janela, 
    text="EDITAR", 
    bg="#454272",
    fg="#ffffff", 
    font=("Arial", 12)
)
botao2.place(x=240, y=500, width=200, height=50)

botao3 = tk.Button(
    janela, 
    text="SAIR",
    fg="#ffffff", 
    bg="#C41C1C", 
    font=("Arial", 12)
)
botao3.place(x=580, y=500, width=200, height=50)

janela.mainloop()
