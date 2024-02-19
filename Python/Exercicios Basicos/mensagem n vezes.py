def main():

    msg = input("Digite a mensagem que pretende escrever: ")
    vezes = int(input("Quantas vezes quer que a mensagem se repita? "))

    for i in range (vezes):
        print (msg)

if __name__ == '__main__':
    main()
