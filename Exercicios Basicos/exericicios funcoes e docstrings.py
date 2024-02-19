# Exercicios em Python 2 (uso de funcoes e docstrings)
#
# docstrings: ver https://www.programiz.com/python-programming/docstrings

# Exercicio 1
# contar o numero de ocorrencias de um caracter numa string
# usar uma docstring
# executar na shell os comandos help() e print() para ver a docstring

# Exercicio 2
# indicar a primeira posicao onde ocorre um caracter numa string

# Exercicio 3
# contar o  numero de espaços existente numa string

# Exercicio 4
# remover espacos existentes numa string

# Exercicio 5
# remover caracteres nao alfabeticos existentes numa string

# Exercicio 6
# escrever uma string considerando apenas os caracteres de ordem par (começa em 0)

# Exercicio 7
# substituir numa string um caracter por outro

# Exercicio 8
# escrever os códigos ascii dos caracteres existentes numa string

# Exercicio 9
# contar o numero de vogais de uma string

# Exercicio 10 
# verificar se uma string (palavra) e um palindromo
# usar uma docstring



def contaOcorrencias(string, c):
    '''
        INFO: Retorna o numero de ocorrencias de um caracter numa string.

        (string, char) -> int
        >>> contaOcorrencias("palavra", 'a')
        3
        >>> contaOcorrencias("palavra", 'e')
        0
    '''

    contador = 0

    for a in string:
        if a == c:
            contador += 1
    return contador


def primeiraPosicao(string, c):
    '''
        INFO: Pesquisa em que posição se encontra pela primeira vez a letra pedida na string (começa no zero).

        (string, char) -> int
        >>> primeiraPosicao("palavra", 'a')
        1
        >>> primeiraPosicao("palavra", 'v')
        4
    '''
    
    posicao = 0
    
    for a in string:
        if a == c:
            return posicao
        else:
            posicao += 1
    return -1 #retorna -1 se nao existir na string a letra pedida


def contaEspacos(string):
    '''
        INFO: Pesquisa quantos espaços em branco existem na string.

        (string) -> int
        >>> contaEspacos("palavra")
        0
        >>> contaEspacos("algoritmia e modelos de programacao")
        4
    '''
    
    espacos = 0
    for c in string:
        if c == ' ':
            espacos += 1
    return espacos


def removeEspacos (string):
    '''
        INFO: Pesquisa os espaços em branco e remove os mesmos da string.

        (string) -> int
        >>> removeEspacos("palavra")
        (mantem se igual pois a frase/palavra nao tem espaços para remover)
        >>> removeEspacos("algoritmia e modelos de programacao")
        "algoritmiaemodelosdeprogramacao"
    '''
    
    s='' #string em branco para contruir a frase sem espaços
    
    for c in string:
        if c != ' ':
            s += c
    return s


def removeNaoAlfabeticos(string):
    '''
        INFO: Pesquisa caracteres nao alfabeticos na frase e remove-os.

        (string) -> int
        >>> removeNaoAlfabeticos("palavra")
        0 (nao remove pois nao tem nenhum caracter nao alfabetico para remover)
        >>> removeNaoAlfabeticos("algoritmia e modelos de programacao 3")
        "algoritmiaemodelosdeprogramacao"
    '''
    
    s=''
    for c in string:
        if c.isalpha():
            s += c
    return s

def caracteresPar(string):
    '''
        INFO: Retorna a frase escrita apenas escrevendo os caracteres que se encontram na posição par.

        (string) -> int
        >>> caracteresPar("palavra")
        "plva"
        >>> caracteresPar("algoritmia e modelos de programacao")
        "agrti  oeo epormco"
    '''

    #print(string[::2]) - escreve a string de dois em dois, começa em zero e termina no final da lista.

    s=''
    for c in range(0,len(string), 2):
        d = string[c]
        s += d
    return s


def substituir(string, f, g):
    '''
        INFO: Substitui um caracter por outro a escolha.

        (string, f, g) -> int
        >>> substituir("palavra", 'a', 'o') 
        "polovro"
        >>> substituir("algoritmia e modelos de programacao", 'a', 'o')
        "olgoritmio e modelos de progromocoo"
    '''

    s=''
    for c in string:
        if c == f:
            s += g
        else:
            s += c
    return s

def codigoAscii(string):
    '''
        INFO: Indica qual o codigo ASCII da string digitada (em cada caracter).

        (string) -> int
        >>> codigoAscii("palavra") 
        Codigo ascii: 112 97 108 97 118 114 97
    '''

    print("O codigo ASCII da respetiva palavra/frase é: ",end='')
    for c in string:
        s = print(ord(c), end=' ')
    for c in string:
        print("\nCaractere  =", c, " Valor ASCII = ", ord(c), end='')


def contarVogais(string):
    '''
        INFO: Conta as vogais contidas na string (maiusculas e minisculas).

        (string) -> int
        >>> contaVogais("palavra") 
        "3 Vogais"
        >>> substituir("algoritmia e modelos de programacao")
        "15 Vogais"
    '''

    contador = 0
    #vogais = 'aeiouAEIOU' - podemos usar com uma nova variavel ou comparar direto no IF

    for a in string: 
      if a in "aeiouAEIOU": 
            contador += 1
    return contador
        

def palindromo(string):
    '''
        INFO: Imoprime e compara a palavra escrita ao contrario para detetar se é um palindromo.

        (string) -> int
        >>> palindromo("palavra") 
        "Não é um palindromo."
        >>> substituir("ovo")
        "É um palindromo."
    '''

    #string = string.lower() - escreve a palavra toda em minusculas
    #if string == string[::-1]: - compara  a string com a string quando é reescrita ao contrario ou seja começa no 1, acaba no final da string e anda de -1 em -1 ou seja ao contrario.
    #    return True
    #else:
    #    return False

    s = "" 
    for i in string: 
        s = i + s
    if s == string:
        print("A palavra digitada é um palindromo.")
    else:
        print("A palavra digitada não é um palindromo.")
    return s

    

def main():

    string = input("Digite uma palavra: ")
    c = input("Digite a letra que pretende contar: ")
    contaOcorrencias(string, c)
    
    print(contaOcorrencias.__doc__)
    print("A letra ", c," aparece | ",contaOcorrencias(string,c), " | vezes na sua frase")

    print(primeiraPosicao.__doc__)
    print("A letra ", c," aparece pela primeira vez na posição | ",primeiraPosicao(string,c), " |")

    
    print(contaEspacos.__doc__)
    print("A frase tem | ",contaEspacos(string), " | espaços.")

    print(removeEspacos.__doc__)
    print("A frase sem espaços fica: ",removeEspacos(string))

    print(removeNaoAlfabeticos.__doc__)
    print("A frase sem caracteres NAO alfabeticos fica: ",removeNaoAlfabeticos(string))

    print(caracteresPar.__doc__)
    print("A frase escrita apenas com caracteres na posiçao par fica: ", caracteresPar(string))


    f = input("Qual o caracter que pretende substituir: ")
    g = input("Pretende substituir o carater por que caracter: ")

    print(substituir.__doc__)
    print("Substituindo a letra pedida a frase fica: ", substituir(string, f, g))

    print(codigoAscii.__doc__)
    codigoAscii(string)
    
    print(contarVogais.__doc__)
    print("\nA palavra/frase tem: ", contarVogais(string), " Vogais.")

    print(palindromo.__doc__)
    print("A palavra/frase ao contrario fica: ", palindromo(string))


if __name__ == '__main__':
    main()

   
