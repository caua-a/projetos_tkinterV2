import ttkbootstrap as tk
from db import Banco

class TelaCadastro:
    def __init__(self):
        self.db = Banco()
        self.janela = tk.Window(themename="cyborg")
        self.janela.geometry("1920x1080")
        self.janela.title("Cadastro")
        self.janela.state("zoomed")
        self.janela.resizable(True, True)
        self.tela_cadastro()

    # ----------------------------------------------------------
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    # ----------------------------------------------------------
    def tela_cadastro(self):
        self.limpar_tela()

        tk.Label(self.janela, text="Cadastro de Usuário", font=("Arial", 40)).place(relx=0.5, rely=0.25, anchor="center")

        tk.Label(self.janela, text="Usuário:", font=("Arial", 20)).place(relx=0.5, rely=0.38, anchor="center")
        self.entry_usuario = tk.Entry(self.janela, width=30, font=("Arial", 20))
        self.entry_usuario.place(relx=0.5, rely=0.43, anchor="center")

        tk.Label(self.janela, text="Senha:", font=("Arial", 20)).place(relx=0.5, rely=0.5, anchor="center")
        self.entry_senha = tk.Entry(self.janela, width=30, font=("Arial", 20), show="*")
        self.entry_senha.place(relx=0.5, rely=0.55, anchor="center")

        tk.Button(self.janela, text="Cadastrar", width=20, padding=(20, 10), command=self.cadastrar).place(relx=0.5, rely=0.63, anchor="center")
        tk.Button(self.janela, text="Voltar", width=20, padding=(20, 10), command=self.voltar_login).place(relx=0.5, rely=0.7, anchor="center")

    # ----------------------------------------------------------
    def cadastrar(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()

        if not usuario or not senha:
            self.mensagem("Preencha todos os campos!", "danger")
            return

        if self.db.usuario_existe(usuario):
            self.mensagem("Usuário já existe!", "warning")
            return

        self.db.cadastrar_usuario(usuario, senha)
        self.mensagem("Usuário cadastrado com sucesso!", "success")

        self.entry_usuario.delete(0, "end")
        self.entry_senha.delete(0, "end")

    # ----------------------------------------------------------
    def voltar_login(self):
        self.janela.destroy()
        from classe import Tela_inicial
        app = Tela_inicial()
        app.run()

    # ----------------------------------------------------------
    def mensagem(self, texto, tipo):
        msg = tk.Label(self.janela, text=texto, font=("Arial", 18), bootstyle=tipo)
        msg.place(relx=0.5, rely=0.8, anchor="center")
        msg.after(2500, msg.destroy)

    # ----------------------------------------------------------
    def run(self):
        self.janela.mainloop()
