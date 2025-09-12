import ttkbootstrap as tk

class Janela_principal:
    """Classe para a criação da self.janela principal"""

    def __init__(self):
        # Criar janela
        self.janela = tk.Window(themename="darkly")

        self.janela.geometry("800x600+100+50")
        self.janela.title("Hello World!")
        self.janela.iconbitmap("01_hello_world/java.ico") 
        self.janela.resizable(True, True)

        # Frame central para organizar tudo
        frame_central = tk.Frame(self.janela)
        frame_central.pack(expand=True)

        # Título
        self.label_titulo = tk.Label(frame_central, 
                                text="Bem Vindo!", 
                                font=("Arial", 24), 
                                style="superhero")
        self.label_titulo.pack(pady=5)

        # Pergunta ao usuário
        self.label_nome = tk.Label(frame_central,
                            text="Digite seu nome abaixo:",
                            font=("Arial", 24),
                            style="superhero")
        self.label_nome.pack(pady=5)

        # Campo de entrada
        self.campo_nome = tk.Entry(frame_central, font=("Arial", 16), 
                            style="darkly")
        self.campo_nome.pack(pady=5)
    
        # Botão Enviar
        self.botao_enviar = tk.Button(frame_central, 
                                text="Enviar", 
                                command=self.mostrar_nome,
                                style='darkly') 
        self.botao_enviar.pack(pady=10)


        # Botão Apagar
        self.botao_apagar = tk.Button(frame_central,
                                text="Apagar",
                                style='darkly', 
                                command=self.apagar)
        self.botao_apagar.pack(pady=10)

        # Resultado
        self.label_resultado = tk.Label(frame_central, 
                                text="", 
                                font=("Arial", 30),
                                style="superhero")
        self.label_resultado.pack(pady=10)



    def run(self):
        """Inicia a self.janela. Mantém aberta."""
        # Iniciar o loop da self.janela
        self.janela.mainloop()


    # Função para apagar o resultado
    def apagar(self):
        """Função que apaga a ultima mensagem"""
        self.label_resultado.pack_forget()



    def mostrar_nome(self):
        """Função que pega o nome digitado na caixa de texto e dá um olá."""
        nome_digitado = self.campo_nome.get()
        self.label_resultado.config(text=f"Olá, {nome_digitado}!")
        self.label_resultado.pack(pady=10)