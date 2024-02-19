def soma(lista):
    s = 0
    for n in lista:
        s += n
    return s

def media(lista):
    m = soma(lista) / len(lista)
    return m

def acimaMedia(lista):
    acima = []
    for num in lista:
        if num > media(lista):
            acima.append(num)
    return acima

def maior(lista):
    lista.reverse()
    return lista [0]

def menor(lista):
    lista.sort()
    return lista [0]   
    
def main():

    lista = [] # cria uma lista vazia, sem valor algum inserido

    n = int(input( "Quantos elementos pretende inserir? ")) # questiona o utilizador quantos valores quer adicionar a lista

    for i in range(n): # cria um ciclo "for" com a quantidade de dados a inserir previamente questionada em cima
        e = int(input( "Insira o elemento {0}: ".format(i+1))) # questiona o utilizador qual o primeiro elemento a inserir na posição 0
        lista.append(e) # adiciona a lista o valor inserido em cada posiçao especifica e volta ao inicio do ciclo "for" para nova insercao da posicao 1

    print("Os numeros escolhidos sao: ", lista) # escreve toda a lista

    print("A soma dos numeros é: ", soma(lista))

    print("A média dos numeros é: {:.2f}".format(media(lista)))

    print("Os numeros acima da média são: ", acimaMedia(lista))

    print("O maior valor escolhido é: ", maior(lista))

    print("O menor valor escolhido é: ", menor(lista))

if __name__ == '__main__':
    main()
