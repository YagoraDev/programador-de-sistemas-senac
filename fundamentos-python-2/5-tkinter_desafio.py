import tkinter                         

janela = tkinter.Tk()                  
janela.geometry("800x600")               
janela.title("Minha primeira janela")    
janela.configure(bg="#F3F3F3")

rotulo = tkinter.Label(                 
    janela, 
    text="DASHBORD", 
    font=("Arial", 20), 
    bg="#363636", 
    fg="#FFFFFF"
)
rotulo.pack(fill=tkinter.X,pady=20)                          



def abrir_segunda_janela():
    janela.destroy()
    
    nova_janela = tkinter.Tk()
    nova_janela.title("Página 2")
    nova_janela.geometry("300x200")

    tkinter.Label(nova_janela, text="Bem-vindo à segunda página!").pack(pady=20)






botao1 = tkinter.Button(
    janela, 
    text="Relatórios",
    border="2",
    font="14",
    command=abrir_segunda_janela
)

botao2 = tkinter.Button(
    janela, 
    text="Vendas",
    font="14",
    border="2px"
)

botao3 = tkinter.Button(
    janela, 
    text="Estoque",
    font="14",
    border="2px"
)

botao4 = tkinter.Button(
    janela, 
    text="Configurações",
    font="14",
    border="2px"
)

botao5 = tkinter.Button(
    janela, 
    text="Sair",
    fg="red",
    border="2px",
    font="14",
    command=janela.destroy
)
botao1.pack(fill=tkinter.X, pady=10, padx=30)
botao2.pack(fill=tkinter.X, pady=10, padx=30)
botao3.pack(fill=tkinter.X, pady=10, padx=30)
botao4.pack(fill=tkinter.X, pady=10, padx=30)
botao5.pack(pady=20)

janela.mainloop()                       

