def main():

    cartao = input("Insira o numero")

    if validateCC(cartao) == 0:
        print("Cartão inválido")
    else:
        print("Cartão válido")

def getNumberFromChar(letra):
    charDict = {
        "0": "0","1": "1", "2": "2","3": "3", "4": "4","5": "5",
        "6": "6","7": "7","8": "8","9": "9","A": "10","B": "11",
        "C": "12","D": "13","E": "14","F": "15","G": "16",
        "H": "17","I": "18","J": "19","K": "20","L": "21",
        "M": "22","N": "23","O": "24","P": "25",
        "Q": "26","R": "27","S": "28","T": "29","U": "30",
        "V": "31","W": "32","X": "33","Y": "34","Z": "35",}
    return int(charDict[letra])

def validateCC(str):
    upperCaseStr = str.upper()
    sum = 0
    secondDigit = 0

    if len(str) != 12:
        return 0
    for i in range(len(str) - 1, -1, -1):
        valor = getNumberFromChar(upperCaseStr[i])
        if secondDigit == 1:
            valor = valor * 2
            if valor > 9:
                valor = valor - 9
        sum = sum + valor
        secondDigit = 1 if secondDigit == 0 else 0
    return (sum % 10) == 0














if __name__ == '__main__':
    main()
