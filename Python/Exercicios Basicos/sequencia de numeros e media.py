def main():

    n = int(input("Insira um valor (termina quando escrever 0 (zero): "))

    contador = 0
    soma = 0

    while n > 0:
        contador += 1
        soma += n
        n = int(input("Insira um valor (termina quando escrever 0 (zero): "))

    media = soma / contador

    print("A media dos numeros é: ", media)
    

if __name__ == '__main__':
    main()

