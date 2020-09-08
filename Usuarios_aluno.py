from Banco_aluno import Banco
  
class Usuarios(object):
  
  
    def __init__(self, idusuario = 0, nome = "", telefone = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
  
  
    def insertUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("insert into usuarios (nome, telefone) values ('" + self.nome + "', '" + self.telefone + "' )")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
  
    def updateUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "' where idusuario = " + self.idusuario + " ")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
  
    def deleteUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
  
    def selectUser(self, idusuario):
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("select * from usuarios where idusuario = " + idusuario + " ")
  
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
