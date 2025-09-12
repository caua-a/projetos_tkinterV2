import tkinter as tk
from classe_bot import Gemini_bot

class Janela_Bot:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("800x600+100+50")
        self.janela.title("Bot Daora")
        self.janela.resizable(True,True)
        self.janela.configure(bg= "#4e4d54")

    
        # FRAME PARA DEIXAR TUDO NO CENTRO DA TELA
        frame_central = tk.Frame(self.janela, bg="#4e4d54")
        frame_central.pack(expand=True)

        # TITULO DO BOT
        self.label_titulo = tk.Label(frame_central,
                                     text="NordestBot",
                                     font=("Trebuchet MS", 40),
                                     fg="yellow",
                                     bg="#4e4d54")
        self.label_titulo.pack(side="top", fill="x")

        # DESCRICAO
        self.label_descrição = tk.Label(frame_central,
                                        text="""Eai cumpadi! Eu sou o NordestBot, um cabra véi arretado que sabe tudo do mundu e que vai lhe ajuda em qualqué duvidinha, visse? Se avexe não que num tem pressa não, meu fi!""",
                                        font=("Segoe UI", 20),
                                        foreground="white",
                                        bg="#4e4d54",
                                        wraplength=600)
        self.label_descrição.pack(side="top", fill="x")

        # TEXTO PERGUNTA
        self.label_pergunta = tk.Label(frame_central,
                                       text= "Faça sua pergunta:",
                                       font=("Trebuchet MS", 20),
                                       foreground= "black",
                                       bg="#4e4d54",
                                       fg="yellow")
                                
        self.label_pergunta.pack(pady=10)

        # CAMPO DE ENTRADA
        self.campo_nome =  tk.Entry(frame_central,
                                    bg="#868688",
                                    font=("Trebuchet MS", 20),
                                    width=40)
        self.campo_nome.pack(pady=5) 


        # FRAME PARA BOTÕES
        frame_botoes = tk.Frame(frame_central, bg="#4e4d54")
        frame_botoes.pack(pady=5)

        # BOTÃO PERGUNTAR 1 
        self.botao_perguntar = tk.Button(frame_botoes,
                                         text="Perguntar",
                                         font=("Trebuchet MS", 13),
                                         bg="#11f050",
                                         bd=2,
                                         command=self.resposta)
        self.botao_perguntar.grid(row=0, column=0, padx=10)
        
        # BOTÃO PERGUNTAR 2
        self.botao_perguntar2 = tk.Button(frame_botoes,
                                         text="Perguntar",
                                         font=("Trebuchet MS", 13),
                                         bg="#d41f15")
        self.botao_perguntar2.grid(row=0, column=1, padx=10)



        self.label_resposta = tk.Label(self.janela,
                                       font=("Arial", 15),
                                       text="RESPOSTA")
        self.label_resposta.pack(pady=(20,0))

     


        #criando o robo
        self.robo = Gemini_bot()    


    def resposta(self):
        pergunta = self.campo_nome.get()
        resposta = self.robo.responder(pergunta)
        self.label_resposta.config(text=resposta)

    

    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    bot = Janela_Bot()
    bot.run()


