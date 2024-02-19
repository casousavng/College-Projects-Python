'''
Multiplicacao Russa

Algoritmo para a multiplicacao de dois numeros inteiros que implica
apenas conhecer a tabuada do 2

Algoritmo - multiplicacao de X por Y

- Dividir (divisao inteira) sucessivamente X por 2 ate' chegar 
  ao quociente 1
- Simultaneamente, multiplicar Y sucessivamente por 2
- Adicionar todos os valores de Y sempre que X e' impar

exemplo: 39 x 79

   X  |  Y
 -----------	
   39 |   79	X e' impar
   19 |  158	X e' impar
    9 |  316	x e' impar
    4 |  632
    2 | 1264
    1 | 2528	X e' impar

  39 x 79 = 79 + 158 + 316 + 2528 = 3081
'''

def multiplicacao_russa(x,y):
    resultado = 0
    while y > 0:
        if y % 2 == 1:
          resultado += x
        x *= 2
        y //= 2
    return resultado


def main():

    x = int(input("Digite o numero X: "))
    y = int(input("Digite o numero Y: "))
    print("O calculo da multiplicação: ", multiplicacao_russa(x,y))


if __name__ == '__main__':
    main()
