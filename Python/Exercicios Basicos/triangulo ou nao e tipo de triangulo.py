def main():


    a = int(input("Insira o lado A: "))
    b = int(input("Insira o lado B "))
    c = int(input("Insira o lado C: "))

    if a+b>c or b+c>a or a+c>b:
        print ("É um triangulo ", end='')
        if a==b==c:
            print ("equilatero")
        elif a==b or a==c or b==c:
            print ("isosceles")
        else:
            print ("escaleno")
    else:
        print ("Não é um triangulo.")


if __name__ == '__main__':
    main()
