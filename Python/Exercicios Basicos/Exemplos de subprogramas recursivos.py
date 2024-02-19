# Exemplos de subprogramas recursivos
'''
Ver:
https://www.python-course.eu/python3_recursive_functions.php
https://www.programiz.com/python-programming/recursion
Advantages of Recursion:
    - Recursive functions make the code look clean and elegant.
    - A complex task can be broken down into simpler sub-problems using recursion.
    - Sequence generation is easier with recursion than using some nested iteration.

Disadvantages of Recursion:
    - Sometimes the logic behind recursion is hard to follow through.
    - Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    - Recursive functions are hard to debug.
'''

''' calculo do produto de dois numeros usando apenas somas
'''
def produto( x, y ):
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    return x + produto( x, y-1 )

''' calculo da soma de dois numeros recorrendo apenas a somas unitarias
'''
def soma( x, y ):
    if y == 0:
        return x
    return 1 + soma( x, y-1 )

''' calculo da potencia: base x, expoente y
'''
def potencia( x, y ):
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * potencia( x, y-1)

''' fatorial de um numero inteiro
'''
def fatorial(x):
    if x == 1 or x == 0:
        return 1
    return x * fatorial(x-1)
    
''' converter de base 10 para base 2
'''
def converte10para2( n ):
    if n > 0:
    	converte10para2( n // 2 )
    	print( n%2, end='' )
    	
def main():
    a = int(input('Insira um numero inteiro: ' ))
    b = int(input('Insira outro numero inteiro: ' ))
    
    p = produto( a, b )
    s = soma( a, b )
    e = potencia( a, b )

    print( 'Produto : ', p )
    print( 'Soma    : ', s )
    print( 'Potencia: ', e )
    print( 'Fatorial de ', a, ': ', fatorial(a) )
    print( b, ' em base binaria: ', end='')
    converte10para2( b )

if __name__ == '__main__':
    main()
