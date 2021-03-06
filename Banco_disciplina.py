import sqlite3

class Banco():
  
    def __init__(self):
        self.conexao = sqlite3.connect('banco_disciplina.db')
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
  
        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement ,
                     nome text,
                     telefone text)""")
        self.conexao.commit()
        c.close()
