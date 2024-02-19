def main():

    moedas = [2,1,0.50,0.20,0.10,0.05,0.02,0.01]
    notas = [100,50,20,10,5]
    i = 0
    preco = float(input("Insira o preco do produto (em euros): "))
    valorPago = float(input("Insira o valor entregue pelo cliente (em euros): "))
    troco = int(valorPago-preco)

    
    

    if preco > valorPago:
        print ("Ainda falta pagar: ", preco-valorPago, "Eur")
    elif preco % valorPago == 0:
        print ("Pagou quantia exata, não tem direito a troco.")
    else:
        print("O troco do cliente são: ", troco, " Eur")
        print("Deve ser dado na seguinte forma:")
        while troco != 0:
            qtd = int(troco/notas[i])
            if qtd != 0:
                if qtd > 1 and notas[i] > 1:
                    print(str(qtd) + " notas de " + str(notas[i])+' €')
                    troco = troco % notas[i]
                elif qtd == 1 and notas[i] > 1:
                    print(str(qtd) + " nota de " + str(notas[i])+' €')
                    troco = troco % notas[i]
                elif qtd > 1 and notas[i] == 1:
                    print(str(qtd) + " notas de " + str(notas[i])+' €')
                    troco = troco % notas[i]
                else:
                    print(str(qtd) + " notas de " + str(notas[i])+' €')
                    troco = troco % notas[i]
            i += 1
        troco = int(round((troco - int(troco))*100,2))
        i = 0
        while troco != 0:
            qtd = int(troco/moedas[i])
            if qtd != 0:
                if qtd > 1 and moedas[i] > 1:
                    print(str(qtd) + " notas de " + str(moedas[i])+' €')
                    troco = troco % moedas[i]
                elif qtd == 1 and moedas[i] > 1:
                    print(str(qtd) + " nota de " + str(moedas[i])+' €')
                    troco = troco % moedas[i]
                elif qtd > 1 and moedas[i] == 1:
                    print(str(qtd) + " notas de " + str(moedas[i])+' €')
                    troco = troco % moedas[i]
                else:
                    print(str(qtd) + " notas de " + str(moedas[i])+' €')
                    troco = troco % moedas[i]
            i += 1







if __name__ == '__main__':
    main()
