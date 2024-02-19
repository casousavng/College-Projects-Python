    ############################################################################################################################
    # A função deste Programa consiste em, com as chaves fornecidas pelo utilizador poder codificar ou                         #
    # descodificar uma mensagem em forma de cifra para ser descodificada apenas com a chave correta                            #
    #                                                                                                                          #
    # Nesta versão removi a informação relativa ao PIN visto nao fazer sentido para o uso geral da aplicação em si.            #
    # Removi ainda todos os comentarios pois o programa em si é identico ao "automatico" criado e enviado                      #                       
    #                                                                                                                          #
    # Realizado na disciplina de Programação e Computadores (1Ano/2Semestre -  Engenharia Informatica) 2022/2023               #
    # Aluno: Carlos André Sousa                                                                                                #
    ############################################################################################################################


from tkinter import *


def main():
    
    chave1 = chave_1.get()
    cifra = cifra1.get()

    if chave1.isalpha() and cifra.isalpha():
        chave1 = chave1.lower()
        cifra = cifra.lower()
        nova_chave1 = repetirChave1(cifra,chave1)
        descodificar(nova_chave1,cifra)
        
    else:
        print("chave invalida")
    
def main2():

    chave2 = chave_2.get()
    frase2 = frase_2.get()
    nova_chave2 = repetirChave2(frase2,chave2)
    codificar(nova_chave2,frase2)

def repetirChave1(cifra, chave1):
    
    num_repeticoes = int(len(cifra)/len(chave1) + 1)
    chave_repetida = chave1 * num_repeticoes
    nova_chave1 = chave_repetida[:len(cifra)]
    return nova_chave1

def repetirChave2(frase2, chave2):
    
    num_repeticoes = int(len(frase2)/len(chave2) + 1)
    chave_repetida = chave2 * num_repeticoes
    nova_chave2 = chave_repetida[:len(frase2)]
    return nova_chave2
    
def descodificar(nova_chave1, cifra):

    valor_chave=[]
    valor_cifra=[]
    valor_mensagem = []
    subtrai = []
    mensagem_final = []
    texto_f=[]

    for c in nova_chave1:
        valor_chave.append(ord(c)-96)

    for c in cifra:
        valor_cifra.append(ord(c)-96)

    for elemChave, elemCifra in zip(valor_cifra, valor_chave):
        subtrai.append(elemCifra + elemChave)
    subtrai = [elemChave - elemCifra for elemChave, elemCifra in zip(valor_cifra, valor_chave)]

    for c in subtrai:
        if c < 0:
            c = c + 26
        valor_mensagem.append(c)
    
    for c in valor_mensagem:
        c = c + 96
        mensagem_final.append(c)
    
    c = [chr(i) for i in mensagem_final]
    for i in c:
        texto_f.append(i)
    texto = ''.join(texto_f)
    resultado.set(texto)

def codificar(nova_chave2, frase2):

    valor_chave2=[]
    valor_frase2=[]
    valor_mensagem2 = []
    soma = []
    mensagem_final2 = []
    mensagem_f2=[]

    for c in nova_chave2:
        valor_chave2.append(ord(c)-96)

    for c in frase2:
        valor_frase2.append(ord(c)-96)

    for elemChave, elemFrase in zip(valor_chave2, valor_frase2):
        soma.append(elemChave + elemFrase)
    soma = [elemChave + elemFrase for elemChave, elemFrase in zip(valor_chave2, valor_frase2)]

    for c in soma:
        if c > 26:
            c = c - 26
        valor_mensagem2.append(c)
    
    for c in valor_mensagem2:
        c = c + 96
        mensagem_final2.append(c)

    c = [chr(i) for i in mensagem_final2]
    for i in c:
        mensagem_f2.append(i)
    texto2 = ''.join(mensagem_f2)
    texto_f.set(texto2)


root = Tk()


root.geometry('520x375')
root.title('Codificador e Descodificador de CIFRAS')
root.resizable(False,False)
texto = Label(text='Chave:',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.06)
chave_1 = StringVar()
entrada_texto = Entry(textvariable=chave_1)
entrada_texto.place(relx=0.25,rely=0.05)
texto = Label(text='Cifra:',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.16)
cifra1 = StringVar()
entrada_texto = Entry(textvariable=cifra1)
entrada_texto.place(relx=0.25,rely=0.15)
texto = Label(text='Mensagem:',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.26)
resultado = StringVar()
resultado_lb = Label(textvariable=resultado,font=("Arial", '12','bold'),fg="gold")
resultado_lb.place(relx=0.25, rely=0.25)
butao = Button(text='Descodificar',command=main)
butao.place(relx=0.05,rely=0.35)
texto = Label(text='____________________________________________________________________',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.45)
texto = Label(text='Chave: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.61)
chave_2 = StringVar()
entrada_texto = Entry(textvariable=chave_2)
entrada_texto.place(relx=0.25,rely=0.60)
texto = Label(text='Mensagem: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.71)
frase_2 = StringVar()
entrada_texto = Entry(textvariable=frase_2)
entrada_texto.place(relx=0.25,rely=0.70)
texto = Label(text='Cifra: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.81)
texto_f = StringVar()
texto_f_lb = Label(textvariable=texto_f,font=("Arial", '12','bold'),fg="red")
texto_f_lb.place(relx=0.25, rely=0.81)
butao = Button(text='Codificar',command=main2)
butao.place(relx=0.05,rely=0.90)
butao = Button(text='SAIR',command=root.destroy)
butao.place(relx=0.80,rely=0.90)
texto = Label(text='criado por Carlos Sousa para ISPGAYA (EI FEV2023)',font=('Arial','8','bold'),fg="green")
texto.place(relx=0.30,rely=0.92)
root.mainloop()

if __name__ == '__main__':
    main()
