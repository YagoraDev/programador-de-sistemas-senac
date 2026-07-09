import tkinter                           # biblioteca nativa do python

janela = tkinter.Tk()                    # Criar janela
janela.geometry("800x600")               # Define o tamanho da tela
janela.resizable(False,False)            # Deixa a janela fixa
janela.title("Minha primeira janela")    # Titulo do programa 
janela.configure(bg="#F3F3F3")

rotulo = tkinter.Label(                  # Criacao do elemento para aparecer na tela
    janela, 
    text="Olá, Mundo!", 
    font=("Arial", 20), 
    bg="#3C28F0", 
    fg="#333333"
)
rotulo.pack(fill=tkinter.X,pady=20)                            # Torna o codigo visivel (empilhar)

botao1 = tkinter.Button(
    janela, 
    text="Clique aqui!"
)

botao2 = tkinter.Button(
    janela, 
    text="Fechar janela", 
    command=janela.destroy
)
botao1.pack(pady=10)
botao2.pack(pady=10)

janela.mainloop()                        # Entra no programa

