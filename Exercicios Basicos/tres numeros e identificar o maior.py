def main():

    n1 = int(input("Insira o primeiro numero: "))
    n2 = int(input("Insira o segundo numero: "))
    n3 = int(input("Insira o terceiro numero: "))

    if n1 > n2 and n1 > n3:
        print ("O numero ", n1, " é o maior dos três números")
    
    if n2 > n1 and n2 > n3:
        print ("O numero ", n2, " é o maior dos três números")

    if n3 > n1 and n3 > n2:
        print ("O numero ", n3, " é o maior dos três números")

if __name__ == '__main__':
    main()
