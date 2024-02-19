from tkinter import *

def getNumberFromChar(letra):
    charDict = {
        "0": "0","1": "1", "2": "2","3": "3", "4": "4","5": "5",
        "6": "6","7": "7","8": "8","9": "9","A": "10","B": "11",
        "C": "12","D": "13","E": "14","F": "15","G": "16",
        "H": "17","I": "18","J": "19","K": "20","L": "21",
        "M": "22","N": "23","O": "24","P": "25",
        "Q": "26","R": "27","S": "28","T": "29","U": "30",
        "V": "31","W": "32","X": "33","Y": "34","Z": "35",}
    return int(charDict[letra])

def validarCC(str):
    
    upperCaseStr = str.upper()
    sum = 0
    secondDigit = 0
    if len(str) != 12:
        return 0
    for i in range(len(str) - 1, -1, -1):
        valor = getNumberFromChar(upperCaseStr[i])
        if secondDigit == 1:
            valor = valor * 2
            if valor > 9:
                valor = valor - 9
        sum = sum + valor
        secondDigit = 1 if secondDigit == 0 else 0
    return (sum % 10) == 0

def validar():
    cartao = numerocc.get()
    if validarCC(cartao) == 0:
        texto = "Cartão inválido!"
    else:
        texto = "Cartão válido!"
    return resultado.set(texto)


root = Tk()
root.geometry('350x300')
root.title('Validar Cartão de Cidadão')
root.resizable(False,False)
numero = StringVar()
texto = Label(text='Número cartão: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.1)

numerocc = StringVar()
entrada_texto = Entry(textvariable=numerocc)
entrada_texto.place(relx=0.42,rely=0.12)

resultado = StringVar()
resultado_lb = Label(textvariable=resultado,font=("Helvetica", '12','bold'),fg="blue")
resultado_lb.place(relx=0.35, rely=0.7)

butao = Button(text='Validar Cartão de Cidadão',command=validar)
butao.place(relx=0.25,rely=0.45)
root.mainloop()
