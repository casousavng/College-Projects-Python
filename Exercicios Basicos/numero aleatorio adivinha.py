#    Adivinhar um numero aleatorio entre 1 e 100, gerado pelo computador num numero maximo e tentativas

import random

def main():

    print("** ADIVINHE O NUMERO **")
    maxTenta = int(input("Numero de tentativas: "))

    tentativas = 0
    numero = random.randint(1, 100)
    print(numero)

    while tentativas < maxTenta:
        tentativas += 1
        adivinha = int(input("Qual o seu palpite: "))
        if adivinha == numero:
            print("PARABENS! Acertou no numero em", tentativas, "tentativas.")
            break
        else:
            if tentativas == maxTenta:
                print ("Acabaram se as tentativas!")
            else:
                print("Continue a tentar!")
                

if __name__ == '__main__':
    main()

