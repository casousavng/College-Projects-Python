def main():

    n = int(input("Insira um numero: "))

    contador = 1
    soma = n

    while contador < 10:
        
        n = int(input("Insira um numero: "))
        soma += n
        contador += 1
        
    media = soma / contador

    print("A soma é: ", soma)
    print("A media dos numeros é: ", media)
    

if __name__ == '__main__':
    main()
