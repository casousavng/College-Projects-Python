def main():

    cifra_original = []
    chaves_teste = []

    # abri o ficheiro cifra.txt e criei uma lista com o texto contido no ficheiro que apesar de ser unico seria mais
    # facil de trabalhar com ela assim pois assim obtenho logo o seu valor chamando a posição inicial da lista (chaves_teste[0])
    # podendo a posterior alterar para usar mais que uma cifra e/ou chave diferente

    ficheiro_cifra = open("cifra.txt", "r")
    for cifra in ficheiro_cifra:
        cifra_original.append(cifra)

    # abri o ficheiro palavras.txt e crie uma nova lista com as 50 palavras fornecidas, foi necessario usar a função .strip() para
    # remover o newline(\n) a cada uma das palavras pois ao serem adicionadas a lista seguiam sempre com \n 
    # (oriundo da criação de nova linha no ficheiro).
    # Como por exemplo: a primeira palavra em vez de ser adicionada como "amor" era adicionada a lista como "amor\n" o que 
    # faria variar os calculos na cifra pois inclui mais um valor a ser calculado.

    ficheiro_chave = open("palavras.txt","r")
    for chave in ficheiro_chave:
        chaves = chave.strip()
        chaves_teste.append(chaves)

    # o ciclo abaixo testa todas as chaves fornecidas contra a cifra original para ser possivel procurar uma frase concreta e com nexo.

    for i in chaves_teste:
        nova_chave = repetirChave(cifra_original[0], i)
        print("Teste para a CHAVE: ",i)
        codigosNumericos(nova_chave, cifra_original[0])

def PIN(mensagem_final):

    # foi criado o sub programa PIN para poder gerar o codigo ASCII dos ultimos dois caracteres da frase.
    # foi adicionada a condição se os numeros gerados tiverem mais de 2 digitos cada, não poderiam ser usados pois o codigo
    # pin da caixa contem apenas 4 algarismos sendo assim 2+2 (2 por cada letra)

    ultimo_caracter = mensagem_final[-1]
    penultimo_caracter = mensagem_final[-2]
    if ultimo_caracter >= 100 or penultimo_caracter >= 100:
        print("\n\nNão é possivel usar o PIN gerado pois contém demasiados digitos (o maximo são 4).")
    else:
        print("\n\nO Codigo PIN (numeraçao ASCII) para abrir a caixa será: ",penultimo_caracter,ultimo_caracter)
    
def repetirChave(cifra, chave):

    # usei esta função para poder repetir a palavra chave o numero de vezes quanto necessaria para ficar 
    # com o comprimento igual a cifra, pois é um dos requisitos para descodificar este tipo de cifra.
    # a chave da cifra tem de ter o mesmo comprimento da cifra sendo que se nao tiver deve ser repetida quantas vezes necessaria.
    
    num_repeticoes = int(len(cifra)/len(chave) + 1)
    chave_repetida = chave * num_repeticoes
    nova_chave = chave_repetida[:len(cifra)]
    return nova_chave
    
def codigosNumericos(nova_chave, cifra):

    valor_chave=[]
    valor_cifra=[]
    valor_mensagem = []
    subtrai = []
    mensagem_final = []

    # para nao criar nova tabela com correspondencias "letra : numero" e ter mais uma função, usei a função ord() que vai buscar o
    # codigo ASCII de cada letra mas subtrai 96 (unidades) para que a letra "a" fosse o numero 1 
    # (1 é o seu numero virtual visto o seu numero real em codigo ASCII ser 97) e comeca-se a contar o alfabeto a partir dai. 
    # exemplo((a=1, b=2, c=3, etc))

    print("\nO codigo numérico da CHAVE é: ",end='')
    for c in nova_chave:
        valor_chave.append(ord(c)-96)
    print(valor_chave)
    print("\n")

    print("O codigo numérico da CIFRA é: ",end='')
    for c in cifra:
        valor_cifra.append(ord(c)-96)
    print(valor_cifra)
    print("\n")

    # usei a função zip para subtrair as duas listas diferentes entre sim com cada valor correspondent.e 
    # exemplo: subtrair o primeiro elemento da lista B com o primeiro elemento da lista A e assim sucessivamente.

    for elemChave, elemCifra in zip(valor_cifra, valor_chave):
        subtrai.append(elemCifra + elemChave)
    subtrai = [elemChave - elemCifra for elemChave, elemCifra in zip(valor_cifra, valor_chave)]

    # neste passo apos ter subtraido os valores entre as duas listas, ao encontrar resultados negativos teria de ser adicionado
    # o valor +26 (unidades) para obter a letra correta correspondente e assim obter o valor real da mensagem

    for c in subtrai:
        if c < 0:
            c = c + 26
        valor_mensagem.append(c)

    print("O codigo numerico da MENSAGEM é: ",valor_mensagem)

    # os valores dados no passo anterior nao eram os valores reais das correspondencias ASCII de cada letra foi necessario adicionar
    # +96 (que ja tinha sido retirados anteriormente) para poder ir buscar as letras corretas no codigo ASCII.
    # (se estivesse a trabalhar com substituição por lista {A:1, B:2} podia apagar este passo.
    
    for c in valor_mensagem:
        c = c + 96
        mensagem_final.append(c)
    print("\n")
    
    # neste passo usei a função chr() para converter a lista dos numeros da mensagem em lista de letras e assim
    # poder eliminar as chavetas e as virgulas criando a mensagem final toda junta para mais facil leitura.
    
    print("A MENSAGEM É: " )
    c = [chr(i) for i in mensagem_final]
    for i in c:
        print(i,end=" ")
    PIN(mensagem_final)
        
    print("\n------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
