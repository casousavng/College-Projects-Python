'''
PROGRAMA DESENVOLVIDO NA DISPICPLINA DE ALGORITMOS E MODELOS DE PROGRAMÇÃO 2022/2023

Este programa foi desenvolvido com o intuito de ler uma sequência de números inteiros negativos
que termina quando for lido o valor 0 ou quando o somatório dos valores lidos for menor ou igual a -50.
O programa escreve a média dos valores lidos se a soma for menor ou igual a -50 ou escreve o número de valores
lidos se a soma for maior que -50. Se forem lidos valores positivos, estes são ignorados.

ALUNO: CARLOS ANDRÉ SOUSA
'''

def media(a,b): # vamos usar um subprograma que designamos de "media()" para calcular a media dos valores inseridos pelo utilizador.

    # Este subprograma aceita dois paramentos para poder realizar a sua função (a estes valores chamamos de paramentros reais)
    # e, no nosso caso ao ser chamado ele usa os paramentros reais "soma" e "contador" obtidos na função main().
    # Aquando a sua chamada os mesmos passam a ser denominados de parametros formais (neste caso apresentados com as letras "a" e "b").
    
    '''
    INFO: Retorna a média dos valores inseridos ou seja o somatorio dos valores
    inseridos dividido pela quantidade de valores inseridos.
    O sub-programa esta estruturado na forma de receber os valores "a" e "b",
    onde "a" é o soma dos valores totais e "b" a contagem dos valores inseridos.

    (num, num) -> int
    >>> media(-10, 1)
    -10
    >>> media(-20, 2)
    -10
    '''
    
    media = a / b
    return media

    # Este é um subprograma do tipo "função" pois retorna um valor (neste caso "media") para poder ser usado na função main().


def main():

    contador = 0
    contador2 = 0
    soma = 0

    while True:
        n = int(input("Insira um valor (termina quando escrever 0 (zero): "))
        if n<0:
            contador += 1
            soma += n
            contador2 += 1
            if soma <= -50:
                break
        elif n==0:
            break
        else:
            print("Insira apenas valores negativos!")
    if soma <= -50:
        print(media.__doc__)
        print("A media dos numeros aceites inseridos é: ", media(soma, contador))
        # o subprograma "media" aceita dois paramentros sendo eles, "soma e "contador" estes são os seus paramentros reais.
    else:
        print("A quantidade de numeros aceites inseridos é: ", contador2)

if __name__ == '__main__':
    main()
