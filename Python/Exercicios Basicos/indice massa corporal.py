def main():

    peso = float(input("Qual o seu peso: "))
    altura = float(input("Qual a sua altura: "))

    imc = peso / (altura ** 2)
                       
    print ("O seu IMC é de: ",imc)



if __name__ == '__main__':
    main()
