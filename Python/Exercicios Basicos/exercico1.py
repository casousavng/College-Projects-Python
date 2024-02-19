def main():
    n = int(input("Insira um numero: "))

    if n == 0:
        print ("Zero")
    elif n%2 == 0:
        print ("Par")
    else:
        print ("Impar")

if __name__ == '__main__':
    main()
