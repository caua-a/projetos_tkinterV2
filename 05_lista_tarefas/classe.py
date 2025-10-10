import ttkbootstrap as tk
from classe_lista import Lista
from db import Banco
class Tela_inicial:
    def __init__(self):
        self.janela = tk.Window(themename="darkly")
        self.janela.geometry("1920x1080")
        self.janela.title("Lista de tarefas")
        
        self.janela.state("zoomed")
        self.janela.resizable(True, True)
        self.tela_login()
        
    def tela_login(self):
        self.usuarios=[]
        # Apaga os widgets com função interna do ttk
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        # BUTTON
        self.botao = tk.Button(self.janela, width=20, text="Entrar", padding=(20,10), command=self.verificador_senha)
        self.botao.place(relx=0.5, rely=0.57, anchor="center")

        # LABEL
        self.texto_login= tk.Label(self.janela,text="Usuário", font=("arial", 20))
        self.texto_senha= tk.Label(self.janela,text="Senha", font=("arial", 20))
        
        # ENTRY
        self.user = tk.Entry(self.janela, width=30, font=("arial", 20))
        self.senha = tk.Entry(self.janela, width=30, font=("arial", 20))

        self.user.place(relx=0.5, rely=0.40, anchor="center" )
        self.senha.place(relx=0.5, rely=0.51, anchor="center" )
        self.texto_login.place(relx=0.5, rely=0.35, anchor="center")
        self.texto_senha.place(relx=0.5, rely=0.46, anchor="center")
        self.texto_senha.lower(self.user)

 # --------------------------------------------------------------------------------------

    def verificador_senha(self):
        self.user_cad = "Godofredo"
        self.senha_cad = "amogirassol"
        self.user_dig = self.user.get()
        self.senha_dig = self.senha.get()
        for widget in self.janela.winfo_children():
            widget.destroy()
        self.login_aceito= tk.Label(self.janela,text="Login feito com sucesso", font=("Arial", 50))
        if self.senha_dig == self.senha_cad and self.user_dig == self.user_cad:
            self.login_aceito.place( relx=0.5, rely=0.5, anchor="center")
            self.voltar = tk.Button(self.janela, width=50,text="Voltar", command=self.tela_login)
            self.voltar.place(relx=0.5, rely=0.57, anchor="center")
            self.entrar_lista = tk.Button(self.janela, width=20, text="Ir para lista de tarefas", command=self.trocar_tela)
            self.entrar_lista.place(relx=0.5, rely=0.75, anchor="center")
        else:
            self.erro = tk.Label(self.janela, text="Login incorreto", font=("Arial", 50))
            self.erro.place(relx=0.5, rely=0.5, anchor="center")
            self.voltar = tk.Button(self.janela, width=50,text="Voltar", command=self.tela_login)
            self.voltar.place(relx=0.5, rely=0.57, anchor="center")


 # --------------------------------------------------------------------------------------

    def trocar_tela(self):
        self.janela.destroy()
        lista_tela = Lista()
        lista_tela.run()

 # --------------------------------------------------------------------------------------

    def run(self):
        """Inicia a self.janela. Mantém aberta."""
        # Iniciar o loop da self.janela
        self.janela.mainloop()




