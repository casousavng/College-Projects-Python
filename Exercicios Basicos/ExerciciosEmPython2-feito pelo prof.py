# Exercicios em Python 2 (uso de funcoes)
#
# Exercicio 1
# contar o numero de ocorrencias de um caracter numa string
# com exemplo de docstring
def contaOcorrencias( string, c ):
    '''
        Retorna o numero de ocorrencias de um caracter numa string.

        (string, char) -> int
        >>> contaOcorrencias( "palavra", 'a' )
        3
        >>> contaOcorrencias( "palavra", 'e' )
        0
    '''
    contador = 0
    for a in string:
        if a == c:
            contador += 1
    return contador

# Exercicio 2
# indicar a primeira posicao onde ocorre um caracter numa string
def primeiraPosicaoCaracter( string, c ):
    posicao = 0
    for a in string:
        if a == c:
            return posicao
        else:
            posicao += 1
    # retorna -1 se c nao existir em string
    return -1
            
# Exercicio 3
# contar o  numero de espaços existente numa string
def contaEspacos( string ):
    espacos = 0
    for c in string:
        if c ==' ':
            espacos += 1
    return espacos

# Exercicio 4
# remover espacos existentes numa string
def removeEspacos( string ):
    s = ''
    for c in string:
        if c != ' ':
            s += c
    return s

# Exercicio 5
# remover caracteres nao alfabeticos existentes numa string
def removeNaoAlfabeticos( string ):
    s = ''
    for c in string:
        if c.isalpha():
            s += c
    return s

# Exercicio 6
# escrever a string considerando apenas os caracteres de ordem par (começa em 0)
def ordemPar( string ):
    print( string[::2])

# Exercicio 7
# substituir na string um caracter por outro
def substitui( string, inicial, final ):
    for i in range(0,len(string)):
        if string[i]==inicial:
            string = string[:i]+final+string[i+1:]
    return string

# Exercicio 8
# escrever os códigos ascii dos caracteres da string
def to_ascii( string ):
    for c in string:
        print( ord( c ) )

# Exercicio 9
# contar o numero de vogais da string
def contaVogais( string ):
    contador = 0
    for c in string:
        if c in 'aeiou':
            contador += 1
    return contador

# Exercicio 10 
# verificar se a string (palavra) e um palindromo
# com exemplo de docstring
def palindromo( string ):
    '''
        Verifica se uma palavra é um palindromo.
        (string) -> boolean
        retorna True se string for um palindromo e
        retorna False em caso contrario
        >>> palindromo( radar )
        True
        >>> palindromo( rodar )
        False
    '''
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False
    
# Exercicio 11
# verificar se e um palindromo - frases completas com
# caracteres de pontuacao: p.e. "Was it a rat I saw?", "Step on no pets"
def palindromoFrase( string ):
    string = string.lower()
    string = removeEspacos( string )
    string = removeNaoAlfabeticos( string )

    if string == string[::-1]:
        return True
    else:
        return False


# funcao principal para demonstracao das funcoes acima
def main():

    s = input("Insira uma sequencia de caracteres: " )

    print( "Ocorrencias de 'o' na string ", s, ": ", contaOcorrencias( s, 'o' ))
    
    print( "Primeira posicao de 'a' na string ", s, ": ", primeiraPosicaoCaracter( s, 'a' ) )
    
    print( "Numero de espaços da string ", contaEspacos( s ) )
    
    print( s, ' sem espacos: ', removeEspacos( s ) )
    
    s1 = "ola?mundo!"
    print( s1, ' so com caracteres alfabeticos: ', removeNaoAlfabeticos( s1 ) )

    print( 'Caracteres de ordem par de ', s, ':')
    ordemPar(s)

    print( "Trocar 'o' por 'x' em 'palindromo':", substitui( 'palindromo', 'o', 'x'))

    print('Codigos ASCII dos caracteres de ', s )
    to_ascii( s )

    print( 'Numero de vogais de ', s , ': ', contaVogais( s ) )

    s1 = "radar"
    if palindromo( s1 ):
        print( s1, "e´um palindromo" )
    else:
        print( s1, "nao e' um palindromo" )

    s1 = "Was it a rat I saw?"
    if palindromoFrase( s1 ):
        print( "A frase ", s1, "e' um palindromo" )
    else:
        print( "A frase ", s1, "nao e' um palindromo" )

    if palindromoFrase( s ):
        print( "A frase ", s, "e' um palindromo" )
    else:
        print( "A frase ", s, "nao e' um palindromo" )


    
# testa se o modulo foi importado
# ou se esta a ser executado como programa principal
# (experimentar chamar a funcao main sem a instrucao if anterior)
#if __name__ == '__main__':
main()
 
 
