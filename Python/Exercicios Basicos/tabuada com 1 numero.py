def main():

    n = int(input("Insira um numero entre 1 e 10: "))
    
    while n < 0 or n > 10:
        print ("Insira um numero entre o intervalo de 1 a 10.")
        n = int(input("Insira um numero entre 1 e 10: "))

    
    for i in range (1,11):
        tab = n * i
        print(n," x ",i," = ",tab)


if __name__ == '__main__':
    main()
