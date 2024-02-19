# resolucao simplificada do exercicio de minimizacao do troco
# so' considera a entrega de moedas
#
def main():
    preco = float(input("Insira o preço do produto (em euros): "))
    vpago = float(input("Insira o montante entregue pelo cliente (em euros): "))
 
    troco = vpago - preco
    print("Troco a receber: ", troco )

    # converte o troco em centimos
    troco = int(troco*100)

    # moedas de € representadas com o valor em centimos
    moedas = [200, 100, 50, 20, 10, 5, 2, 1 ]

    print("Moedas a entregar: ")
    i = 0
    while troco > 0:
        n = troco // moedas[i]
        if n>0:
            print( n, " moedas de ", moedas[i]/100, " €" )
        troco = troco % moedas[i]
        i = i + 1

if __name__ == '__main__':
    main()
