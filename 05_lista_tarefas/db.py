import sqlite3

class Banco:
    def __init__(self, nome_banco="tarefas.sqlite"):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.criar_tabela_usuarios()
        self.criar_tabela_tarefas()

    def criar_tabela_usuarios(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def criar_tabela_tarefas(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            concluido INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()

    def cadastrar_usuario(self, usuario, senha):
        self.cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        self.conn.commit()

    def usuario_existe(self, usuario):
        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = ?", (usuario,))
        return self.cursor.fetchone() is not None

    def verificar_login(self, usuario, senha):
        self.cursor.execute("SELECT id FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        return self.cursor.fetchone() is not None

    def adicionar_tarefa(self, nome):
        self.cursor.execute("INSERT INTO tarefas (nome, concluido) VALUES (?, 0)", (nome,))
        self.conn.commit()

    def listar_tarefas(self):
        self.cursor.execute("SELECT id, nome, concluido FROM tarefas")
        return self.cursor.fetchall()

    def concluir_tarefa(self, tarefa_id):
        self.cursor.execute("UPDATE tarefas SET concluido = 1 WHERE id = ?", (tarefa_id,))
        self.conn.commit()

    def excluir_tarefa(self, tarefa_id):
        self.cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        self.conn.commit()
