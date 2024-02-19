
'''
Subprograma para calculo da media

nome do subprograma: calcula_media
tipo do subprograma: funcao
parametros formais : lista_numeros
parametros reais   : numeros
'''

def calcula_media(lista_numeros):
    '''
        Calcula a media de uma lista de numeros

        (lista de numeros inteiros) -> float

        >>> calcula_media( [1, 2, 3] )
        2.0
        >>> calcula_media( [1, 2] )
        1.5
    '''
    return sum(lista_numeros) / len(lista_numeros)

def main():
    numeros = []
    soma = 0
    numero_valores = 0

    while True:
        n = int(input("Insira um numero negativo (0 para terminar): "))

        if n == 0:
            break
        elif n > 0:
            print( "Valor positivo inserido, nao sera' considerado" )
            continue
        else:
            numeros.append(n)
            soma += n
            numero_valores += 1
            if soma <= -50:
                break

    if soma <= -50:
        print("Soma inferior a -50. Média: ", calcula_media(numeros))
    else:
        print("Numero de valores lidos: ", numero_valores)

if __name__ == '__main__':
    main()
