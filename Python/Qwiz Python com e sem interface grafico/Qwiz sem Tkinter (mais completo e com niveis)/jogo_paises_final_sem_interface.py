import random
import time

def main():

    lista = []
    paises = []

    # abre o ficheiro correspondente e associa os nomes dos (paises:capitais) numa lista chamada "lista"
    # de seguida pega nesses mesmos nomes que estao unidos por : (dois pontos) e divide os mesmo numa lista de duas colunas uma para paises e outra para capitais
    
    ficheiro_lista = open("lista_paises_mundo.txt", "r")
    
    for i in ficheiro_lista:
        i = i.strip()
        lista.append(i)
    ficheiro_lista.close()

    for i in lista:
        i = i.split(":")
        paises.append(i)

    print("")

    print(
    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'    
    ' $$$$$$$$$$     ------------------------                                                                      $$$$$$$$\n'
    '  $$$$$$$$$   | QUEM QUER SER MILIONARIO |   [ Edição Capitais Mundiais ]    by Carlos Sousa ISPGAYA          $$$$$$$\n'
    ' $$$$$$$$$$     ------------------------                                                                      $$$$$$$$ \n'
    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
    )
    print(
    
    'Neste programa serão geradas diversas perguntas de escolha multipla onde por cada questão respondida corretamente\n'
    'recebe 3, 2 ou 1 ponto consoante a resposta certa seja dada na primeira, segunda ou terceira tentativa.\n'
    'Se responder erradamente por três vezes na mesma questão, passa a questão seguinte sem pontuar nessa mesma questão.\n'
    'No final sera apresentada a sua pontuação total. Vamos testar o seu conhecimento :)\n'
    
    )

    iniciar = input("Vamos Começar? (S) para Sim, (N) para Não: " )
    print("")


    if iniciar == 'S' or iniciar == 's':

        perguntas = int(input("A quantas questões pretende responder? (Um limite razoavel): "))
        print("")
        
        print(
        'Qual o nivel de dificuldade que pretende jogar?\n'
        'Nivel 1 - Apenas paises Europeus\n'
        'Nivel 2 - Paises Europeus e Americanos (Norte e Sul)\n'
        'Nivel 3 - Todos os Paises do Mundo\n'
        )
        teste_dificuldade = False
        escolha_errada = 0 

        while teste_dificuldade == False:
            dificuldade = int(input("Escolha a dificuldade digitando 1, 2 ou 3 respetivamente: "))
            if dificuldade <= 0 or dificuldade >= 4:
                print("Escolha entre uma das opções disponiveis!")
                print("")
                escolha_errada += 1
            elif escolha_errada > 0:
                print("")
                print("Depois de",escolha_errada,"tentativas agora sim vamos começar!!!")
                break
            else:
                break
        
        if dificuldade == 1:
            print("")
            print("Boa escolha, seguimos entao para as questões sobre paises da Europa!")
            print("")
            quiz(paises, 51,perguntas) # no meu ficheiro portado para a lista a posição [0] até a posição [51] assume apenas paises da Europa
        elif dificuldade == 2:
            print("")
            print("Assim é que é falar, dominamos a Europa e conquistamos as Americas, mas conhecemos as capitais?")
            print("")
            quiz(paises, 106,perguntas) # no meu ficheiro portado para a lista a posição [0] até a posição [106] assume apenas paises da Europa e Americas
        elif dificuldade == 3:
            print("")
            print("O NIVEL MAXIMO, agora sim vamos ver se domina o Mundo e as suas capitais.")
            print("")
            quiz(paises, 239,perguntas) # no meu ficheiro portado para a lista a posição [0] até a posição [239] assume todos os paises do Mundo
        else:
            print("Escolha entre uma das opções disponiveis!")
            print("")
            dificuldade = input("Escolha a dificuldade digitando 1, 2 ou 3 respetivamente: ")

    elif iniciar == 'N' or iniciar == 'n':
        print("Volte quando se sentire mais preparado.")
        print("Vai ver que não é assim tão dificil e acima de tudo é divertido.")
    else:
        print("")
        print("Opção ERRADA: Escolha apenas (S) para Sim ou (N) para Não.")
        print("")
        main()
    

def quiz(paises,nivel,perguntas):

    numero_questoes = 0
    pontos_certos = 0
    pontos_errados = 0

    while numero_questoes < perguntas:

        numero_questoes += 1

        #gera o nome do pais e associa a respetiva capital correta para realizar o quiz
        # o "nivel" vem da funçao main onde é pedido a dificuldade e passa a ser entre 0 e 239
        a = random.randint(0, nivel)
        pais_pergunta = paises[a][0]
        capital_correta = paises[a][1]
        
        #random para escolha da pergunta correta numa posição diferente a cada jogada
        random_pergunta = random.choice(['A','B','C','D']); 

        #gera o nome de tres capitais de paises para as respostas erradas e verifica se alguma delas é igual a capital correta e entre si e se for faz nova variação
        capital_aleatoria1 = paises[random.randint(0,nivel)][1]
        capital_aleatoria2 = paises[random.randint(0,nivel)][1]
        capital_aleatoria3 = paises[random.randint(0,nivel)][1]

        while (capital_aleatoria1 == capital_correta) or (capital_aleatoria2 == capital_correta) or (capital_aleatoria3 == capital_correta) or (capital_aleatoria1 == capital_aleatoria2) or (capital_aleatoria2 == capital_aleatoria3) or (capital_aleatoria3 == capital_aleatoria1):
            capital_aleatoria1 = paises[random.randint(0,nivel)][1]
            capital_aleatoria2 = paises[random.randint(0,nivel)][1]
            capital_aleatoria3 = paises[random.randint(0,nivel)][1]
            
            
       
        #gera a pergunta inicial para questionar a capital do pais e o numero da questão em que se encontra.
        print("[ Questão",numero_questoes,"]")
        
        #print("Qual a capital de " + str(pais_pergunta)+"?","(CORRETA:" + str(capital_correta)+")")
        #desbloquear o print() acima para obter a pergunta com a resposta associada, apenas usada no desenvolvimento e testes do programa
        print("Qual a capital de " + str(pais_pergunta)+"?")

        #organiza o QUIZ nas quatro posições de escolha diferentes e imprime no ecra
        if random_pergunta == 'A':
            print("A - " + str(capital_correta))
            #time.sleep(0.5)
            print("B - " + str(capital_aleatoria1))
            print("C - " + str(capital_aleatoria2))
            print("D - " + str(capital_aleatoria3))
        if random_pergunta == 'B':
            print("A - " + str(capital_aleatoria1))
            print("B - " + str(capital_correta))
            print("C - " + str(capital_aleatoria2))
            print("D - " + str(capital_aleatoria3))
        if random_pergunta == 'C':
            print("A - " + str(capital_aleatoria1))
            print("B - " + str(capital_aleatoria2))
            print("C - " + str(capital_correta))
            print("D - " + str(capital_aleatoria3))
        if random_pergunta == 'D':
            print("A - " + str(capital_aleatoria1))
            print("B - " + str(capital_aleatoria2))
            print("C - " + str(capital_aleatoria3))
            print("D - " + str(capital_correta))

        resposta = input("Resposta correta: " )

        acertou = False
        tentativas = 3
        pontos = 4

        # usei este trecho para formatação de texto quando a pontuação e as tentativas estao no singular ou no plural.
        if pontos == 1:
            texto_ponto = "ponto."
        else:
            texto_ponto = "pontos."

        if tentativas == 1:
            texto_tentativa = "tentativa."
        else:
            texto_tentativa = "tentativas."

        #inicia o ciclo while para a verificação das respostas dadas as perguntas previamente emitidas
        while tentativas > 0 or acertou == False or numero_questoes > 0:
            
            tentativas -= 1
            pontos -= 1

            if random_pergunta == 'A' and (resposta == 'A' or resposta == 'a'):
                print("")
                print("Certissimo!!! Voce acaba de receber", pontos, texto_ponto)
                pontos_certos += 3
                acertou = True
                break
            elif random_pergunta == 'B' and (resposta == 'B' or resposta == 'b'):
                print("")
                print("Certissimo!!! Voce acaba de receber", pontos, texto_ponto)
                pontos_certos += 3
                acertou = True
                break
            elif random_pergunta == 'C' and (resposta == 'C' or resposta == 'c'):
                print("")
                print("Certissimo!!! Voce acaba de receber", pontos, texto_ponto)
                pontos_certos += 3
                acertou = True
                break
            elif random_pergunta == 'D' and (resposta == 'D' or resposta == 'd'):
                print("")
                print("Certissimo!!! Voce acaba de receber", pontos, texto_ponto)
                pontos_certos += 3
                acertou = True
                break
            elif random_pergunta != 'A' or 'B' or 'C' or 'D':
                if tentativas == 0:
                    pontos_certos += 2
                    print("")
                    print("NÃO é essa a resposta correta!!! No entanto não tem mais tentativas!")
                    print("")
                    break
                print("")
                print("NÃO é essa a resposta correta!!! Tem mais", tentativas, texto_tentativa)
                pontos_errados += 1
                
            resposta = input("Resposta correta: " )

        if pontos_certos > 1:
            texto_pontos = "pontos"
        else:
            texto_pontos = "ponto"

        # no caso de gastar as tres tentativas por pergunta ou se o jogo terminal pelo limite das perguntas segue o techo abaixo        
        if numero_questoes == perguntas:

            percentagem = (pontos_certos-pontos_errados)*100/(perguntas*3)
            print("")
            print(" $$$$$$$$$$$ O seu Jogo ACABOU! $$$$$$$$$$$ ")
            print("")
            print("Concluiu as suas",perguntas,"jogadas com sucesso.")
            print("A sua PONTUAÇÃO FINAL foi de", (pontos_certos)-(pontos_errados), texto_pontos,"em",(perguntas*3),"pontos possiveis.")
            print("Obteve uma percentagem de respostas corretas de ","%.2f" % percentagem+"%")
            if perguntas >= 7:
                if percentagem < 50:
                    print("Precisa de estudar um pouco mais, mas vai conseguir.")
                elif percentagem >=50 and percentagem <= 99:
                    print("Nada mau, obteve mais de 50% das respostas corretas, esta no bom caminho.")
                else:
                    print("PARABENS! Nunca pensei que sabia tanto sobre cidades e capitais, mas experimente um nivel mais dificil para ver se conhece mesmo tudo.")
            else:
                print("Experimente escolher um nivel superior ou até mais questões, concerteza que vai gostar da surpresa.")
            print("")
        elif not acertou:
            print("Nada esta perdido! Passemos então a pergunta seguinte.")
            print("")
        else:
            print("A sua PONTUAÇÃO ATUAL é de", (pontos_certos)-(pontos_errados), texto_pontos+".")
            print("")


if __name__ == '__main__':
    main()
