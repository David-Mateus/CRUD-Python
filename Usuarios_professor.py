from Banco_professor import Banco
  
class Usuarios(object):
  
  
    def __init__(self, idusuario = 0, nome = "", cpf = "", departamento = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.cpf = cpf
        self.departamento = departamento

  
    def insertUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("insert into usuarios (nome, cpf, departamento) values ('" + self.nome + "', '" + self.cpf + "', '" + self.departamento + "' )")
  
            banco.conexao.commit()
            c.close()
  
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
  
    def updateUser(self):
  
        banco = Banco()
        try:
  
            c = banco.conexao.cursor()
  
            c.execute("update usuarios set nome = '" + self.nome + "', cpf = '" + self.cpf + "', departamento = '" + self.departamento + "' where idusuario = " + self.idusuario + " ")
  
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
                self.cpf = linha[2]
                self.departamento = linha[3]
                self.usuario = linha[4]
  
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
