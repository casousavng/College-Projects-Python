def main():

    n = int(input("Insira um numero positivo e maior que zero: "))

    if n > 0:
        
        n = int(input("Insira um numero: "))
        soma += n
        contador += 1
        
    media = soma / contador

    print("A soma é: ", soma)
    print("A media dos numeros é: ", media)
    

if __name__ == '__main__':
    main()
