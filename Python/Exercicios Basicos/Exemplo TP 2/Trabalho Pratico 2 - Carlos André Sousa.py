
'''
PROGRAMA DESENVOLVIDO NA DISPICPLINA DE ALGORITMOS E MODELOS DE PROGRAMÇÃO 2022/2023

Este programa foi desenvolvido com o intuito de ler uma sequência de números inteiros impares e não negativos
que termina quando for lido o valor 0 ou quando o total de valores lidos chegar a 10.
O programa escreve o numero de valores lidos no caso desse numero ser inferior a 10 ou escreve a média dos
valores impares e nao negativos que foram lidos.
Se forem lidos valores negativos ou numeros pares estes devem ser ignorados, nao entrando na contagem de valores.

ALUNO: CARLOS ANDRÉ SOUSA
DATA: 16 de Janeiro de 2023
'''

# parametros reais: soma e contador
# parametros formais: "a" e "b"
# nome do subprograma: media(a,b)
# tipo de subprograma: procedimento (pois não retorna um valor usavel)

def media(a,b): # vamos usar um subprograma que designamos de "media()" para calcular a media dos valores inseridos pelo utilizador.

    # Este subprograma aceita dois paramentos para poder realizar a sua função (a estes valores chamamos de paramentros reais)
    # e, no nosso caso ao ser chamado ele usa os paramentros reais "soma" e "contador" obtidos na função main().
    # Aquando a sua chamada os mesmos passam a ser denominados de parametros formais (neste caso apresentados com as letras "a" e "b").
    
    '''
    INFO: Retorna a média dos valores inseridos ou seja o somatorio dos valores
    inseridos dividido pela quantidade de valores inseridos.
    O sub-programa esta estruturado na forma de receber os valores "a" e "b",
    onde "a" é o soma dos valores totais inseridos conforme as condições
    e "b" a contagem dos valores inseridos conforme as condiçoes.

    (a, b) -> int
    media = a / b
    >>> media(30, 10)
    3
    >>> media(70, 10))
    7
    '''
    
    media = a / b
    print("A media dos numeros inseridos e aceites é: ", media)


    # Este é um subprograma do tipo "procedimento" pois não retorna um valor para ser usado na função main(), ele escreve o valor.


def main():

    contador1 = 0
    contador2 = 0
    soma = 0

    while True:
        n = int(input("Insira um valor positivo e impar (termina quando escrever 0 (zero): "))
        if n > 0 and n%2 != 0 :
            contador1 += 1
            soma += n
            contador2 += 1
            if contador1 >= 10:
                break
        elif n==0:
            break
        else:
            print("Insira apenas valores positivos e impares!")
    if contador1 >= 10:
        print(media.__doc__)
        media(soma, contador1)
        # o subprograma "media" aceita dois paramentros sendo eles, "soma e "contador" estes são os seus paramentros reais.
    else:
        print("A quantidade de numeros inseridos e aceites é: ", contador2)

if __name__ == '__main__':
    main()
