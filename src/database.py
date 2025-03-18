import sqlite3

# Criar e conectar ao banco de dados
conn = sqlite3.connect("dados.db", check_same_thread=False)
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS dicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    descricao TEXT NOT NULL
)
""")
conn.commit()

def add_dica(url, descricao):
    """Adiciona uma nova dica ao banco de dados"""
    cursor.execute("INSERT INTO dicas (url, descricao) VALUES (?, ?)", (url, descricao))
    conn.commit()

def get_dicas():
    """Retorna todas as dicas salvas"""
    cursor.execute("SELECT id, url, descricao FROM dicas")
    return cursor.fetchall()

def update_dica(dica_id, url, descricao):
    """Atualiza uma dica no banco de dados"""
    cursor.execute("UPDATE dicas SET url = ?, descricao = ? WHERE id = ?", (url, descricao, dica_id))
    conn.commit()

def delete_dica(dica_id):
    """Remove uma dica do banco de dados"""
    cursor.execute("DELETE FROM dicas WHERE id = ?", (dica_id,))
    conn.commit()
