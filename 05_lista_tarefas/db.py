import sqlite3
class Banco:
    def __init__(self, nome_banco= "tarefas.sqlite"):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()

    def criar_tabela(self):
        self.cursor.execute("CREATE TABLE tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, concluido INTEGER DEFAULT 0)")
        self.conn.commit()
