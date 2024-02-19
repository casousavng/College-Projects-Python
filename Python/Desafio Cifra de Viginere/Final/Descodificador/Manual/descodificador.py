
from tkinter import *

def main():
    
    chave = chave1.get()
    cifra = cifra1.get()
    nova_chave = repetirChave(cifra,chave)
    descodificar(nova_chave,cifra)

def repetirChave(cifra, chave):

    # usei esta função para poder repetir a palavra chave o numero de vezes quanto necessaria para ficar 
    # com o comprimento igual a cifra, pois é um dos requisitos para descodificar este tipo de cifra.
    
    num_repeticoes = int(len(cifra)/len(chave) + 1)
    chave_repetida = chave * num_repeticoes
    nova_chave = chave_repetida[:len(cifra)]
    return nova_chave
    
def descodificar(nova_chave, cifra):

    valor_chave=[]
    valor_cifra=[]
    valor_mensagem = []
    subtrai = []
    mensagem_final = []

    # para nao criar nova tabela com correspondencias "letra : numero" e ter mais uma função, usei a função ord() que vai buscar o
    # codigo ASCII de cada letra mas subtrai 96 (unidades) para que a letra "a" fosse o numero 1 (numero virtual visto o real ser 97)
    # e comeca-se a contar o alfabeto a partir dai. (a=1, b=2, c=3, etc)

    for c in nova_chave:
        valor_chave.append(ord(c)-96)

    for c in cifra:
        valor_cifra.append(ord(c)-96)

    # usei a função zip para subtrair as duas listas diferentes com cada valor correspondente 
    # exemplo: subtrair o primeiro elemento da lista B com o primeiro elemento da lista A e assim sucessivamente.

    for elemChave, elemCifra in zip(valor_cifra, valor_chave):
        subtrai.append(elemCifra + elemChave)
    subtrai = [elemChave - elemCifra for elemChave, elemCifra in zip(valor_cifra, valor_chave)]

    # neste passo apos ter subtraido os valores entre as duas listas, ao encontrar resultados negativos teria de ser adicionado
    # o valor 26 (unidades) para obter a letra correta correspondente e assim obter o valor real da mensagem

    for c in subtrai:
        if c < 0:
            c = c + 26
        valor_mensagem.append(c)

    # Os valores dados no passo anterior nao eram os valores reais das correspondencias ASCII de cada letra foi necessario adicionar
    # +96 (que ja tinha sido retirados anteriormente) para poder ir buscar as letras corretas no codigo ASCII.
    # (se estivesse a trabalhar com substituição por lista {A:1, B:2} podia apagar este passo.
    
    for c in valor_mensagem:
        c = c + 96
        mensagem_final.append(c)
    
    # Neste passo usei a função chr() para converter a lista de codigos ASCII da mensagem em lista de letras e ainda assim
    # poder eliminar as chavetas e as virgulas criando a mensagem final toda junta para mais facil leitura.

    mensagem_f=[]
    
    c = [chr(i) for i in mensagem_final]
    for i in c:
        mensagem_f.append(i)
    texto = ''.join(mensagem_f)
    
    codigo_pin = mensagem_final[-1], mensagem_final[-2]

    resultado.set(texto)
    pin.set(codigo_pin)


    

root = Tk()
root.geometry('500x190')
root.title('Descodificador de CIFRAS')
root.resizable(False,False)

texto = Label(text='CHAVE: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.10)
chave1 = StringVar()
entrada_texto = Entry(textvariable=chave1)
entrada_texto.place(relx=0.25,rely=0.1)

texto = Label(text='CIFRA: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.25)
cifra1 = StringVar()
entrada_texto = Entry(textvariable=cifra1)
entrada_texto.place(relx=0.25,rely=0.25)

texto = Label(text='MENSAGEM: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.40)
resultado = StringVar()
resultado_lb = Label(textvariable=resultado,font=("Arial", '12','bold'),fg="blue")
resultado_lb.place(relx=0.25, rely=0.4)

texto = Label(text='PIN DO COFRE: ',font=('Arial','12','bold'))
texto.place(relx=0.05,rely=0.55)
pin = StringVar()
pin_lb = Label(textvariable=pin,font=("Arial", '12','bold'),fg="red")
pin_lb.place(relx=0.25, rely=0.55)

butao = Button(text='DESCODIFICAR',command=main)
butao.place(relx=0.05,rely=0.73)

butao = Button(text='SAIR',command=root.destroy)
butao.place(relx=0.32,rely=0.73)

texto = Label(text='criado por Carlos Sousa para ISPGAYA (EI FEV2023)',font=('Arial','8','bold'),fg="green")
texto.place(relx=0.57,rely=0.9)

root.mainloop()

if __name__ == '__main__':
    main()
