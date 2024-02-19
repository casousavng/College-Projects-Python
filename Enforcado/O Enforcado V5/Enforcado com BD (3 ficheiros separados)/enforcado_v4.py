import turtle
import random

def enforcado(errado): #subprograma para construção do enforcado
    
    tentativa = errado
    turtle.pencolor("green")

    if tentativa == 1: 
        # desenhar a cabeça
        turtle.goto(-75, 240)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15)
        turtle.penup()
        
    elif tentativa == 2:
        # desenhar o tronco
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
        turtle.goto(-75, 190)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()

    elif tentativa == 4:
        # desenhar o segundo braço
        turtle.goto(-75, 190)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    
    elif tentativa == 5:
        # desenhar a primeira perna
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
        turtle.goto(-75, 170)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

def apagar(): # sub programa para limpar o enforcado na forca

    turtle.speed(1000)
    turtle.pencolor("white")
    turtle.pensize(5)

    # apaga a cabeça na forca
    turtle.home()
    turtle.goto(-75, 240)
    turtle.right(90)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(15)
    turtle.penup()
    
    # apaga o tronco na forca
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
    
    # apaga o primeiro braço na forca
    turtle.goto(-75, 190)
    turtle.pendown()
    turtle.left(55)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.penup()
    
    # apaga o segundo braço na forca
    turtle.goto(-75, 190)
    turtle.pendown()
    turtle.left(70)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.penup()
    
    # apaga a primeira perna na forca
    turtle.goto(-75, 200)
    turtle.pendown()
    turtle.left(55)
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(60)
    turtle.penup()
    
    # apaga a segunda perna na forca
    turtle.goto(-75, 170)
    turtle.pendown()
    turtle.right(120)
    turtle.forward(60)
    turtle.penup()
        
def morto(): # subprograma para desenhar o enforcado "morto"
    
    turtle.speed(1000)
    turtle.pencolor("red")
    turtle.pensize(3)

    # desenhar a cabeça a vermelho
    turtle.home()
    turtle.goto(-70, 240)
    turtle.right(90)
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

def vivo(): # subprograma para criar o enforcado "vivo" fora da forca

    turtle.speed(1000)
    turtle.pencolor("green")
    turtle.pensize(3)

    # desenhar a cabeça fora da forca
    turtle.home()
    turtle.goto(85, 235)
    turtle.pendown()
    turtle.right(180)
    turtle.circle(15)
    turtle.penup()

    # desenhar o tronco fora da forca
    turtle.goto(85, 235)
    turtle.pendown()
    turtle.left(90)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(30)
    turtle.penup()

    # desenhar o primeiro braço fora da forca
    turtle.goto(85, 185)
    turtle.pendown()
    turtle.left(55)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.penup()

    # desenhar o segundo braço fora da forca
    turtle.goto(85, 185)
    turtle.pendown()
    turtle.left(70)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.penup()

    # desenhar a primeira perna fora da forca
    turtle.goto(85, 185)
    turtle.pendown()
    turtle.left(55)
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(60)
    turtle.penup()

    # desenhar a segunda perna fora da forca
    turtle.goto(85, 155)
    turtle.pendown()
    turtle.right(120)
    turtle.forward(60)
    turtle.penup()

    turtle.pencolor("black")

def jogo(nome, nivel, pontuacao, jogadas):

    turtle.pencolor("black")

    if nivel == 1:
        ficheiro = "facil.txt"
    if nivel == 2:
        ficheiro = "medio.txt"
    if nivel == 3:
        ficheiro = "dificil.txt"

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

    #abre o ficheiro correspondente conforme foi escolhido acima nas opcoes de nivel, copia o conteudo para um vetor e fecha o ficheiro

    palavras = []
    pontos = 100
    
    ficheiro_palavras = open(ficheiro,"r")
    for palavra in ficheiro_palavras:
        palavra = palavra.strip().lower()
        palavras.append(palavra)
    ficheiro_palavras.close()

    palavra = random.choice(palavras) #escolhe a palavra ao acaso do ficheiro correspondente

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

        letra = turtle.textinput('O ENFORCADO','Digita uma letra:') # caixa de texto para inserção da letra

        while letra =="" or letra == None:
            letra = turtle.textinput('O ENFORCADO','Digita uma letra:') # mostra novamente a caixa de texto se nao for inserida nenhuma letra
        
        turtle.goto(posicao,-150)
        turtle.pencolor("black")
        if letra not in certo: #vai adicionando as letras colocadas corretamente ao vetor "certo" e imprimindo na posição correta
            for i in palavra:
                if i == letra:
                    turtle.write(letra.upper() + ' ', True, font=("Courier", 16, "normal")) # imrpime na tela a letra certa na posição
                    certo += letra
                else:
                    turtle.write('_ ', True, font=("Courier", 16, "normal")) # errando a letra volta a imprimir o espaço dela
                    
        if letra not in palavra: #vai contabilizando as respostas erradas e "enforcando o boneco" chamando a sub funçao enforcado e subtraindo os pontos a 100
            errado += 1
            pontos -= 16.66
            enforcado(errado)
            
        if errado == 6: # ao fim de 6 tentativas, completa a palavra com as letras que faltam e transmite a mensagem de erro e desenha o boneco "morto"
            turtle.goto(posicao,-150)
            turtle.pencolor("black")
            for i in palavra:
                if i in certo:
                    turtle.write('_ ', True, font=("Courier", 16, "normal"))
                else:
                    turtle.write(i.upper() + ' ', True, font=("Courier", 16, "normal"))
                    
            turtle.goto(0, -200)
            turtle.pencolor("red")
            turtle.write(nome + ', infelizmente perdeste!', False, align='center', font=("Courier", 20, "normal"))
            turtle.goto(0, -230)
            turtle.write('Mas tenta novamente, da próxima vais conseguir.', False, align='center', font=("Courier", 16, "normal"))
            apagar()
            morto()
            jogadas +=1
            
        if len(certo) == len(palavra): #compara os comprimentos da palavra com o comprimentos das letras que se acertou
            turtle.pencolor("green")
            turtle.goto(0, -200)
            turtle.write('Parabéns ' + nome + '! Encontras-te a palavra certa.', False, align='center', font=("Courier", 20, "bold"))
            turtle.goto(0, -230)
            turtle.write('Acertaste com uma precisão de ' + str("{:.2f}".format(pontos)) + '%', False, align='center', font=("Courier", 16, "normal"))
            apagar()
            vivo()
            jogadas +=1
            pontuacao +=1
            terminar = True

    resposta = turtle.textinput('O ENFORCADO','Queres jogar novamente? (s / n): ')

    while resposta != 's' and resposta != 'n':
        resposta = turtle.textinput('O ENFORCADO','Escolhe apenas "s" para Sim ou "n" para Não: ')
    if resposta == 's':
        turtle.clear()
        jogo(nome,nivel,pontuacao,jogadas)
    elif resposta == 'n':
        turtle.clear()
        turtle.pencolor("green")
        turtle.goto(0, 37)
        turtle.write('Obrigado por Jogares!', False, align='center', font=("Courier", 25, "bold"))
        turtle.goto(0, 0)
        turtle.write('Espero ver-te novamente ' + nome + '.', False, align='center', font=("Courier", 25, "normal"))
        turtle.goto(0, -35)
        turtle.write('A pontuação total jogada no nivel ' + str("{:.0f}".format(nivel)) + ' foi de '+ str(pontuacao) + '/' + str(jogadas) + '.', False, align='center', font=("Courier", 20, "normal"))
        terminar = True

def main():

    turtle.hideturtle() # esconde a cursor da tartaruga
    turtle.speed(5) # velocidade de contrução do desenho em 5
    turtle.pensize(3) # espessura da caneta em 3
    turtle.pencolor("black") # cor da caneta
    turtle.title("O ENFORCADO by Carlos Sousa ISPGAYA") # titulo da tela
    turtle.bgcolor("white") # cor da tela

    pontuacao = 0
    jogadas = 0

    # texto de incicio de jogo onde aparece o cumprimento ao jogador e as instruções
    turtle.penup()
    turtle.home()
    turtle.goto(0, 200)
    turtle.write('Bem-vindo ao Jogo', False, align='center', font=("Courier", 30, "normal"))
    turtle.goto(0, 147)
    turtle.pencolor("green")
    turtle.write('O ENFORCADO', False, align='center', font=("Courier", 46, "bold"))
    turtle.pencolor("black")
    turtle.goto(0, -170)
    turtle.write('Este jogo é muito simples, primeiro escolhes o nivel que pretendes jogar', False, align='center', font=("Courier", 14, "normal"))
    turtle.goto(0, -190)
    turtle.write('sendo que tens 3 niveis á escolha entre Fácil, Médio e Dificil, escolhe bem.', False, align='center', font=("Courier", 14, "normal"))
    turtle.goto(0, -220)
    turtle.write('De seguida tentas adivinhar a palavra inserindo as letras do alfabeto mas', False, align='center', font=("Courier", 14, "normal"))
    turtle.goto(0, -240)
    turtle.write('cuidado pois sempre que errares o Enforcado sofre a consequencia. Boa sorte :)', False, align='center', font=("Courier", 14, "normal"))

    # requisição do nome do jogador e nivel, compara ainda se o nome esta vazio e se o nivel escolhido esta entre 1 e 3
    
    nome = turtle.textinput('Qual é o teu nome?','')
    while nome =="" or nome == None:
        nome = turtle.textinput('Não me dizes o teu nome?','')     
        
    nivel = turtle.numinput('Qual o Nivel que pretendes jogar?','1 - Facil  |  2 - Médio  |  3 - Dificil')
    while nivel != 1 and nivel != 2 and nivel !=3:
        nivel = turtle.numinput('Escolhe entre os niveis disponiveis.','1 - Facil  |  2 - Médio  |  3 - Dificil')

    turtle.clear() # limpa a tela para dar inicio ao jogo
    
    jogo(nome, nivel, pontuacao, jogadas) # chama a subfunção jogo enviando os parametros inseridos

if __name__ == '__main__':
    main()
