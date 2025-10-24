import ttkbootstrap as tk
from db import Banco
from classe_cadastro import TelaCadastro

class Tela_inicial:
    def __init__(self):
        self.db = Banco()
        self.janela = tk.Window(themename="cyborg")
        self.janela.geometry("1920x1080")
        self.janela.title("Login")
        self.janela.state("zoomed")
        self.janela.resizable(True, True)
        self.tela_login()

    # ----------------------------------------------------------
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    # ----------------------------------------------------------
    def tela_login(self):
        self.limpar_tela()
        self.janela.title("Login")

        tk.Label(self.janela, text="Login", font=("Arial", 40)).place(relx=0.5, rely=0.25, anchor="center")

        tk.Label(self.janela, text="Usuário:", font=("Arial", 20)).place(relx=0.5, rely=0.38, anchor="center")
        self.entry_user = tk.Entry(self.janela, width=30, font=("Arial", 20))
        self.entry_user.place(relx=0.5, rely=0.43, anchor="center")

        tk.Label(self.janela, text="Senha:", font=("Arial", 20)).place(relx=0.5, rely=0.5, anchor="center")
        self.entry_senha = tk.Entry(self.janela, width=30, font=("Arial", 20), show="*")
        self.entry_senha.place(relx=0.5, rely=0.55, anchor="center")

        tk.Button(self.janela, text="Entrar", width=20, padding=(20, 10), command=self.verificar_login).place(relx=0.5, rely=0.63, anchor="center")
        tk.Button(self.janela, text="Cadastrar", width=20, padding=(20, 10), command=self.abrir_cadastro).place(relx=0.5, rely=0.7, anchor="center")

    # ----------------------------------------------------------
    def abrir_cadastro(self):
        self.janela.destroy()
        cadastro = TelaCadastro()
        cadastro.run()

    # ----------------------------------------------------------
    def verificar_login(self):
        usuario = self.entry_user.get().strip()
        senha = self.entry_senha.get().strip()

        if not usuario or not senha:
            self.mensagem("Preencha todos os campos!", "danger")
            return

        if self.db.verificar_login(usuario, senha):
            self.tela_tarefas()
        else:
            self.mensagem("Usuário ou senha incorretos!", "danger")

    # ----------------------------------------------------------
    def tela_tarefas(self):
        self.limpar_tela()
        self.janela.title("Lista de Tarefas")

        tk.Label(self.janela, text="Lista de Tarefas", font=("Arial", 40)).place(relx=0.5, rely=0.15, anchor="center")

        self.entry_tarefa = tk.Entry(self.janela, width=40, font=("Arial", 18))
        self.entry_tarefa.place(relx=0.5, rely=0.25, anchor="center")

        tk.Button(self.janela, text="Adicionar", padding=(10, 5), command=self.adicionar_tarefa).place(relx=0.5, rely=0.3, anchor="center")
        tk.Button(self.janela, text="Sair", padding=(10, 5), command=self.tela_login).place(relx=0.9, rely=0.1, anchor="center")

        self.frame_tarefas = tk.Frame(self.janela)
        self.frame_tarefas.place(relx=0.5, rely=0.55, anchor="center")

        self.atualizar_lista_tarefas()

    # ----------------------------------------------------------
    def adicionar_tarefa(self):
        nome = self.entry_tarefa.get().strip()
        if nome:
            self.db.adicionar_tarefa(nome)
            self.entry_tarefa.delete(0, "end")
            self.atualizar_lista_tarefas()

    # ----------------------------------------------------------
    def atualizar_lista_tarefas(self):
        for widget in self.frame_tarefas.winfo_children():
            widget.destroy()

        tarefas = self.db.listar_tarefas()
        for x, (tarefa_id, nome, concluido) in enumerate(tarefas):
            cor = "success" if concluido else "secondary"
            tk.Label(self.frame_tarefas, text=nome, font=("Arial", 16), bootstyle=cor).grid(row=x, column=0, padx=10, pady=5)

            if not concluido:
                tk.Button(self.frame_tarefas, text="Concluir", command=lambda id=tarefa_id: self.concluir_tarefa(id)).grid(row=x, column=1, padx=5)
            tk.Button(self.frame_tarefas, text="Excluir", command=lambda id=tarefa_id: self.excluir_tarefa(id)).grid(row=x, column=2, padx=5)

    # ----------------------------------------------------------
    def concluir_tarefa(self, tarefa_id):
        self.db.concluir_tarefa(tarefa_id)
        self.atualizar_lista_tarefas()

    # ----------------------------------------------------------
    def excluir_tarefa(self, tarefa_id):
        self.db.excluir_tarefa(tarefa_id)
        self.atualizar_lista_tarefas()

    # ----------------------------------------------------------
    def mensagem(self, texto, tipo):
        msg = tk.Label(self.janela, text=texto, font=("Arial", 18), bootstyle=tipo)
        msg.place(relx=0.5, rely=0.8, anchor="center")
        msg.after(2500, msg.destroy)

    # ----------------------------------------------------------
    def run(self):
        self.janela.mainloop()
