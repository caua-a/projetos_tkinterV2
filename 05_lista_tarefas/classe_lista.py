import ttkbootstrap as tk
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




    def run(self):
    # Iniciar o loop da self.janela
        self.janela.mainloop()




if __name__ == "__main__":
    bot = Lista()
    bot.run()
