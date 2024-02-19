def main():

    chave = "programa"
    cifra = "yfhaauhuekjwwsvphhdsaurddarvyblbufvlfinsysxuxpenqlxjs" 

    nova_chave = repetirChave(cifra, chave)
    
    codigoNumerico(nova_chave, cifra)

def repetirChave(cifra, chave):

    # usei esta função para poder repetir a palavra chave o numero de vezes quanto necessaria para ficar 
    # com o comprimento igual a cifra, pois é um dos requisitos para descodificar este tipo de cifra.
    
    num_repeticoes = int(len(cifra)/len(chave) + 1)
    chave_repetida = chave * num_repeticoes
    nova_chave = chave_repetida[:len(cifra)]
    return nova_chave
    
def codigoNumerico(nova_chave, cifra):

    valor_chave=[]
    valor_cifra=[]
    valor_mensagem = []
    subtrai = []
    mensagem_final = []

    # para nao criar nova tabela com correspondencias "letra : numero" e ter mais uma função, usei a função ord() que vai buscar o
    # codigo ASCII de cada letra mas subtrai 96 (unidades) para que a letra "a" fosse o numero 1 (numero virtual visto o real ser 97)
    # e comeca-se a contar o alfabeto a partir dai. (a=1, b=2, c=3, etc)

    print("O codigo numerico da respetiva CHAVE é: ",end='')
    for c in nova_chave:
        valor_chave.append(ord(c)-96)
    print(valor_chave)

    print("O codigo numerico da respetiva CIFRA é: ",end='')
    for c in cifra:
        valor_cifra.append(ord(c)-96)
    print(valor_cifra)

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

    print("O codigo numerico da respetiva MENSAGEM é: ",valor_mensagem)

    # os valores dados no passo anterior nao eram os valores reais das correspondencias ASCII de cada letra foi necessario adicionar
    # 96 (que ja tinha sido retirados anteriormente) para poder ir buscar as letras corretas.
    # se estivesse a trabalhar com substituição por lista podia apagar este passo.
    
    for c in valor_mensagem:
        c = c + 96
        mensagem_final.append(c)

    # neste passo usei a função chr() para converter a lista dos numeros da mensagem em lista de letras e assim
    # e eliminar as chavetas e as virgulas criando a mensagem de mais facil leitura.
    
    print("A Mensagem é: " ,end='')
    c = [chr(i) for i in mensagem_final]
    for i in c:
        print(i,end=" ")

if __name__ == '__main__':
    main()
