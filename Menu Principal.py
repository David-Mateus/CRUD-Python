from tkinter import*
import sqlite3

def cadastro_alunos():
    from App_alunos import Application
    # cadastro_alunos

    
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute ("select * from aluno")

    


    cursor.execute('''insert into aluno (nome, cpf)
                values(?, ?)''', (nome,  cpf))
    conexao.commit()
    cursor.close()
    conexao.close()

    
def cadastro_professor():
    from App_professor import Application

    
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute ("select * from usuarios")



    cursor.execute('''insert into banco (nome, cpf, departamento)
                values(?, ?, ?)''', (nome, cpf, departamento))

    conexao.commit()
    cursor.close()
    conexao.close()


def cadastra_disciplina():
    from App_disciplina import Application
    
    conexão = sqlite3.connect("disciplina.db")
    cursor = conexão.cursor()
    
    cursor.execute("select * from disciplina")
    cursor.execute(''' insert into disciplina(nome, codigo)
                 values(?,?)''',(nome,codigo))

    conexao.commit()
    cursor.close()
    conexao.close()


def cadastra_turma():
    from App_turma import Application  #importando class do codigo principal da turma

    
    conexão = sqlite3.connect("turma.db")
    cursor = conexão.cursor()
    
    cursor.execute("select * from turma")
    cursor.execute(''' insert into disciplina(nome, codigo)
                 values(?,?)''',(nome,codigo))

    conexao.commit()
    cursor.close()
    conexao.close()

 #TKinter menu    
janela = Tk()

bt1 = Button(janela, width=0, text="  Cadastro de Alunos  ",
    command=cadastro_alunos)
bt1.place(x=23, y=100)

bt2 = Button(janela, width=0, text="  Cadastro de Professor  ",
    command=cadastro_professor)
bt2.place(x=17, y=40)

bt6 = Button(janela, width=0, text="  Cadastro de Disciplina ",
    command=cadastra_disciplina)
bt6.place(x=18, y=70)

bt3 = Button(janela, width=0, text="  Listar turmas ",
    command=cadastra_turma)
bt3.place(x=40, y=130)


    

janela.geometry("170x170")
janela.title(" Menu ")
janela.mainloop()
