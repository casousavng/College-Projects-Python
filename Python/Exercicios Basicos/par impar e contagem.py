def main():

    n = int(input("Insira um numero inteiro: "))
    pares = 0
    impares =0

    while n > 0:

        if n%2==0:
            pares += 1
        else:
            impares += 1
        n = int(input("Insira um numero inteiro: "))
        

    print ("Contagem de numeros pares: ", pares)
    print ("Contagem do numeros impares: ", impares)
                














if __name__ == '__main__':
    main()
