from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

parent = Tk()
parent.eval('tk::PlaceWindow . center')

parent.withdraw()

nome = simpledialog.askstring('Nome', 'Insira o nome: ', parent=parent)
idade = simpledialog.askinteger('Idade', 'Insira a idade: ', minvalue=0, maxvalue=100, parent=parent)

mensagem = 'Olá ' + str(nome) + ', parabéns pelos seus ' + str(idade) + ' anos.'

info = messagebox.showinfo( 'Mensagem de Parabéns', mensagem, parent=parent)

parent.mainloop()
parent.destroy()
