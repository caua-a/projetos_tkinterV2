import tkinter as tk


class Calculadora_imc:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("800x600+100+50")
        self.janela.title("Calculadora IMC")
        self.janela.resizable(True,True)
        self.janela.configure(bg= "#4e4d54")
        self.lbl_resultado = tk.Label(self.janela, text="", font=("arial", 20))
        self.lbl_resultado.pack(padx=100, pady=100)
        
        frame_central = tk.Frame(self.janela, bg="#4e4d54")
        frame_central.pack(expand=True)

        #ENTRADA PESO
        self.label_peso = tk.Label(frame_central,
                                     text="Digite seu peso em kg:",
                                     font=("Segoe UI", 15),
                                     fg="white",
                                     bg="#4e4d54")
        self.label_peso.pack(pady=(10))

        #ENTRADA PESO
        self.entry_peso = tk.Entry(frame_central,
                                   bg="#fff",
                                   font=("Segoe UI", 10),
                                   width=30)
        self.entry_peso.pack(pady=5)
        
        #TEXTO ALTUA
        self.label_altura = tk.Label(frame_central,
                                     text="Digite sua altura em Metros:",
                                     font=("Segoe UI", 15),
                                     fg="white",
                                     bg="#4e4d54")
        self.label_altura.pack(pady=(10))

        #ENTRADA ALTURA
        self.entry_altura = tk.Entry(frame_central,
                                   bg="#FFF",
                                   font=("Segoe UI", 10),
                                   width=30)
        self.entry_altura.pack(pady=5)
 
        self.botao_enviar = tk.Button(frame_central,
                                      text="Enviar",
                                      bg="#8a8a8d",
                                      width= 15,
                                      height=2,
                                      command=self.calculo)
        self.botao_enviar.pack(pady=5)


    def calculo(self):
        
        try:
            peso = float(self.entry_peso.get())  
            altura = float(self.entry_altura.get())
            resultado = peso / (altura ** 2)
            if resultado < 18.5:
                status = "Abaixo do peso"
                cor = "orange"
            elif resultado < 25:
                status = "Peso normal (saudável)"
                cor = "green"
            elif resultado < 30:
                status = "Sobrepeso"
                cor = "orange"
            elif resultado < 35:
                status = "Obesidade grau I"
                
                cor = "red"
            elif resultado < 40:
                status = "Obesidade grau II"
                cor = "red"
            else:
                status = "Obesidade grau III"
                cor = "red"
            self.lbl_resultado.config(text=f"IMC: {resultado:.2f} - {status}", fg=cor)
        except:
            self.lbl_resultado.config(text="Erro: digite um número válido", fg="red")
            

    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    bot = Calculadora_imc()
    bot.run()
