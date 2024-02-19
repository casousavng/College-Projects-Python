import turtle
import random


def enforcado(errado): #subprograma para construção do enforcado
    
    tentativa = errado
    
    if tentativa == 1: 
        # desenhar a cabeça
        turtle.pencolor("green")
        turtle.goto(-75, 240)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15)
        turtle.penup()
        
    elif tentativa == 2:
        # desenhar o tronco
        turtle.pencolor("green")
        turtle.goto(-75, 240)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
        
    elif tentativa == 3:
        # desenhar o primeiro braço
        turtle.pencolor("green")
        turtle.goto(-75, 190)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()

    elif tentativa == 4:
        # desenhar o segundo braço
        turtle.pencolor("green")
        turtle.goto(-75, 190)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    
    elif tentativa == 5:
        # desenhar a primeira perna
        turtle.pencolor("green")
        turtle.goto(-75, 200)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
   
    elif tentativa == 6:
        # desenhar a segunda perna
        turtle.pencolor("green")
        turtle.goto(-75, 170)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()
        
def morto(errado):
    
    turtle.speed(100)
    tentativa = errado
    
    if tentativa == 6:

        # desenha a forca no inicio do jogo mas sem a pintar pois so me interessa pintar o boneco
        turtle.penup()
        turtle.home()
        turtle.left(90)
        turtle.forward(100)
        turtle.forward(175)
        turtle.left(90)
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(35)

        turtle.pencolor("white")
        turtle.pensize(5)

        # apaga a cabeça
        turtle.goto(-75, 240)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15)
        turtle.penup()
        # apaga o tronco
        turtle.goto(-75, 240)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
        # apaga o primeiro braço
        turtle.goto(-75, 190)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
        # apaga o segundo braço
        turtle.goto(-75, 190)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
        # apaga a primeira perna
        turtle.goto(-75, 200)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
        # desenhar a segunda perna
        turtle.goto(-75, 170)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

        turtle.pencolor("black")
        turtle.pensize(3)

        # desenha a forca no inicio do jogo mas sem a pintar pois so me interessa pintar o boneco
        turtle.penup()
        turtle.home()
        turtle.left(90)
        turtle.forward(100)
        turtle.forward(175)
        turtle.left(90)
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(35)

        turtle.pencolor("red")
        turtle.pensize(3)

        # desenhar a cabeça a vermelho
        turtle.goto(-70, 240)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15)
        turtle.penup()
        # desenhar o tronco a vermelho
        turtle.goto(-75, 240)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.penup()
        # desenhar o primeiro braço a vermelho
        turtle.home()
        turtle.goto(-75, 205)
        turtle.pendown()
        turtle.left(255)
        turtle.forward(45)
        turtle.penup()
        # desenhar o segundo braço a vermelho
        turtle.home()
        turtle.goto(-75, 205)
        turtle.pendown()
        turtle.right(75)
        turtle.forward(48)
        turtle.penup()
        # desenhar a primeira perna a vermelho
        turtle.home()
        turtle.goto(-75, 170)
        turtle.pendown()
        turtle.left(265)
        turtle.forward(60)
        turtle.penup()
        # desenhar a segunda perna a vermelho
        turtle.home()
        turtle.goto(-75, 170)
        turtle.pendown()
        turtle.left(275)
        turtle.forward(63)
        turtle.penup()

def main():

    turtle.hideturtle() # esconde a cursor da tartaruga
    turtle.speed(3) # velocidade de contrução do desenho em 3
    turtle.pensize(3) # espessura da caneta em 3
    turtle.pencolor("black") # cor da caneta
    turtle.title("O ENFORCADO by Carlos Sousa ISPGAYA") # titulo da tela
    turtle.bgcolor("white") # cor da tela

    # desenha a forca no inicio do jogo
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(100)
    # até este ponto o desenho é apenas movido para nao ficar sobreposto com a caixa de texto e so a partir daqui é construido
    turtle.left(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    
    palavras = ['livro','escola','professor','cadeira','secretaria',
                'biblioteca','matematica','programaçao','exames']
    
    palavra = random.choice(palavras) #escolhe a palavra ao acaso da lista de palavras sugerida acima

    # centra a palavra consoante o seu comprimento (total dividido por 2) no ecra principal
    
    posicao = (0-(len(palavra)/2) * 18)
    turtle.goto(posicao,-150)

    # aplica os espaços "_" necessarios para o comprimento da palavra que foi atribuida

    for i in palavra:
        turtle.pencolor("black")
        turtle.write('_ ', True, font=("Courier", 16, "normal"))

    certo = [] # vetor que guarda as letras corretas quando o jogador acerta
    errado = 0 # contador de respostas erradas que fara o desenho consoante o numero de respostas erradas (limite é 6)
    terminar = False
    
    while errado < 6 and not terminar:
        letra = turtle.textinput('ENFORCADO','Digita uma letra:') # caixa de texto para inserção da letra
        
        turtle.goto(posicao,-150)
        turtle.pencolor("black")
        if letra not in certo: #vai adicionando as letras colocadas corretamente ao vetor "certo"
            for i in palavra:
                if i == letra:
                    turtle.write(letra.upper() + ' ', True, font=("Courier", 16, "normal"))
                    certo += letra
                else:
                    turtle.write('_ ', True, font=("Courier", 16, "normal"))
                    
        if letra not in palavra: #vai contabilizando as respostas erradas e "enforcando o boneco" chamando a sub funçao enforcado
            errado += 1
            enforcado(errado)
            
        if errado == 6: # ao fim de 6 tentativas, completa a palavra com as letras que faltam
            turtle.goto(posicao,-150)
            turtle.pencolor("black")
            for i in palavra:
                if i in certo:
                    turtle.write('_ ', True, font=("Courier", 16, "normal"))
                else:
                    turtle.write(i.upper() + ' ', True, font=("Courier", 16, "normal"))
                    
            turtle.goto(0, -200)
            turtle.pencolor("red")
            turtle.write('Infelizmente perdeste! Mas tenta novamente.', False, align='center', font=("Courier", 20, "normal"))
            morto(errado)
            
        if len(certo) == len(palavra):
            turtle.goto(0, -200)
            turtle.pencolor("green")
            turtle.write('Parabens! Encontras-te a palavra certa.', False, align='center', font=("Courier", 20, "normal"))
            terminar = True

    resposta = turtle.textinput('ENFORCADO','Queres jogar novamente? (s / n): ')

    while resposta != 's' and resposta != 'n':
        resposta = turtle.textinput('ENFORCADO','Escolhe apenas "s" para sim ou "n" para não: ')
    if resposta == 's':
        turtle.clear()
        main()
    elif resposta == 'n':
        turtle.clear()
        turtle.home()
        turtle.pencolor("green")
        turtle.write('Obrigado por Jogares!', False, align='center', font=("Courier", 25, "normal")) 
        terminar = True

if __name__ == '__main__':
    main()
