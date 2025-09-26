import ttkbootstrap as tk
from tkinter import Listbox

class Lista:
    def __init__(self):
        self.janela = tk.Window(themename="darkly")
        self.janela.geometry("1920x1080")
        self.janela.title("Lista de tarefas")
        self.janela.state("zoomed")
        self.janela.resizable(True, True)
        self.tela_lista()


    def tela_lista(self):
        self.frame_central = tk.Frame(self.janela, height=1080,width=1500, bootstyle= "dark")
        self.frame_central.pack(pady=100, padx=150, anchor="center")
        self.frame_central.pack_propagate(False)

        self.texto = tk.Label(self.frame_central,text="Lista de tarefas", font=("Arial", 40), bootstyle= "inverse-dark")
        self.texto.pack(side="top")
        self.tarefa_digitar = tk.Entry(self.frame_central, width= 20, font=("arial", 20) ) 
        self.tarefa_digitar.place(relx=0.5, rely=0.2, anchor="center") 
        self.frame_interno = tk.Frame(self.frame_central, height=450, width=800)
        self.frame_interno.place(rely=0.6, relx=0.5, anchor="center")
        self.botao_pegar_tarefa = tk.Button(self.frame_central, width=10, text="Adicionar", padding=(20,10), command= self.lista )
        self.botao_pegar_tarefa.place(relx=0.5, rely=0.28, anchor="center")
        self.botao_remover=tk.Button(self.frame_central, width=10, text="Remover", padding=(20,10), command= self.remover)
        self.botao_remover.place(relx=0.4, rely=0.28, anchor="center")
        self.botao_concluir=tk.Button(self.frame_central, width=10, text="Concluir", padding=(20,10), command= self.concluir)
        self.botao_concluir.place(relx=0.6, rely=0.28, anchor="center")
        self.itens=Listbox(self.frame_interno, width=50, height=20)
        self.itens.place(relx=0.5, rely=0.5, anchor="center")

    def lista(self):
        self.itens_lista = self.tarefa_digitar.get()
        self.itens.insert("end", f"[  ] {self.itens_lista}")
        self.tarefa_digitar.delete(0,"end")

    def remover(self):
        self.selecionado = self.itens.curselection()
        if self.selecionado:
            self.itens.delete(self.selecionado[0])
        else:
            None

    def concluir(self):
        self.concluido=self.itens.curselection()
        self.tarefa_concluida = str(self.itens.get(self.itens.curselection())).strip(' [ ]')
        if self.concluido:
            self.itens.delete(self.concluido[0])
            self.itens.insert(self.concluido[0], f"[x] {self.tarefa_concluida}")
            


    def run(self):
    # Iniciar o loop da self.janela
        self.janela.mainloop()




if __name__ == "__main__":
    bot = Lista()
    bot.run()
