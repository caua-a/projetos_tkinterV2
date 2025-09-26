import sqlite3

class Banco:
    def __init__(self, nome_banco="tarefas.sqlite"):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.criar_tabela()  # cria a tabela ao inicializar

    def criar_tabela(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            concluido INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()

    def adicionar_tarefa(self, nome):
        self.cursor.execute("INSERT INTO tarefas (nome) VALUES (?)", (nome,))
        self.conn.commit()

    def remover_tarefa(self, id):
        self.cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
        self.conn.commit()

    def concluir_tarefa(self, id):
        self.cursor.execute("UPDATE tarefas SET concluido = 1 WHERE id = ?", (id,))
        self.conn.commit()

    def listar_tarefas(self):
        self.cursor.execute("SELECT id, nome, concluido FROM tarefas")
        return self.cursor.fetchall()

    def fechar(self):
        self.conn.close()
