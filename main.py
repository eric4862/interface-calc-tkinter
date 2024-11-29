from tkinter import *

def calcular(op):
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        if op == 'soma':
            resultado = v1 + v2
            mensagem.config(text="Resultado: " + str(resultado), fg="black")
        elif op == 'subtracao':
            resultado = v1 - v2
            mensagem.config(text="Resultado: " + str(resultado), fg="black")
        elif op == 'multiplicacao':
            resultado = v1 * v2
            mensagem.config(text="Resultado: " + str(resultado), fg="black")
        elif op == 'divisao':
            if v2 != 0:
                resultado = v1 / v2
                mensagem.config(text="Resultado: " + str(resultado), fg="black")
            else:
                mensagem.config(text="Erro: Divisão por zero não é permitida.", fg="red")
                return
        
        campo3.config(state='normal')
        campo3.delete(0, END)
        campo3.insert(0, resultado)
        campo3.config(state='readonly')
    except ValueError:
        mensagem.config(text="Erro: Por favor, insira números válidos.", fg="red")

def somar():
    calcular('soma')

def subtrair():
    calcular('subtracao')

def multiplicar():
    calcular('multiplicacao')

def dividir():
    calcular('divisao')

def entrar():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == "pato" and senha == "1234":
        mensagem_login.config(text="Acesso permitido! Bem-vindo!", fg="green")
        janela_calculadora.deiconify()
        janela_login.withdraw()
    else:
        mensagem_login.config(text="Acesso negado. Tente novamente.", fg="red")

janela_login = Tk()
janela_login.title("Login")
janela_login.geometry("300x150")

Label(janela_login, text="Usuário:").grid(row=0,column=0)
campo_usuario = Entry(janela_login)
campo_usuario.grid(row=0,column=1)

Label(janela_login, text="Senha:").grid(row=1,column=0)
campo_senha = Entry(janela_login, show='*')
campo_senha.grid(row=1,column=1)

botao_entrar = Button(janela_login, text="Entrar", command=entrar)
botao_entrar.grid(row=2,columnspan=2)

mensagem_login = Label(janela_login, text="", fg="red")
mensagem_login.grid(row=3,columnspan=2)

janela_calculadora = Toplevel()
janela_calculadora.title("Calculadora")
janela_calculadora.geometry("300x250")
janela_calculadora.withdraw()

Label(janela_calculadora, text="Valor 1:").grid(row=0,column=0)
campo1 = Entry(janela_calculadora)
campo1.grid(row=0,column=1)

Label(janela_calculadora, text="Valor 2:").grid(row=1,column=0)
campo2 = Entry(janela_calculadora)
campo2.grid(row=1,column=1)

Label(janela_calculadora, text="TOTAL:").grid(row=3,column=0)
campo3 = Entry(janela_calculadora)
campo3.grid(row=3,column=1)
campo3.config(state='readonly')

mensagem = Label(janela_calculadora, text="", fg="red")  
mensagem.grid(row=4,columnspan=2)

Button(janela_calculadora, text="Somar", command=somar).grid(row=5,column=0)
Button(janela_calculadora, text="Subtrair", command=subtrair).grid(row=5,column=1)
Button(janela_calculadora, text="Multiplicar", command=multiplicar).grid(row=6,column=0)
Button(janela_calculadora, text="Dividir", command=dividir).grid(row=6,column=1)

janela_login.mainloop()