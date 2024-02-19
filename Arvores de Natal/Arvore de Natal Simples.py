def main():

    #linhas = int(input('Acredita no Pai Natal? '))
    print ("Gosta de arvores de natal?")
    print("1 - SIM")
    print("2 - NÃO")
    print("3 - TALVEZ")
    resposta = int(input())


    match resposta:
        case 1:

            linhas = int(input('Escolha a altura da sua arvores [entre 7 e 12]? '))
            if linhas < 7 or linhas > 12:
                print("Altura Incorreta! Escolha entre os valores sugeridos para melhor vizualização.")
            else:    
                print()
                for i in range(linhas-4):
                    for j in range(linhas-i):
                        print("  ", end=' ')
                    for k in range(2*i+1):
                        print(" ◉",end=' ')
                    print()
                    
                for i in range(linhas-2):
                    for j in range(linhas-i):
                        print("  ", end=' ')
                    for k in range(2*i+1):
                        print(" ◉",end=' ')
                    print()
                        

                for i in range(linhas):
                    for j in range(linhas-i):
                        print("  ", end=' ')
                    for k in range(2*i+1):
                        print(" ◉",end=' ')
                    print()

                for i in range(linhas-4):
                    for j in range(linhas-1):
                        print("  ", end=' ')
                    print('  ◼︎◼◼◼︎◼︎')

                print()
                print("      ◘◘◘◘◘   ◘◘◘◘◘◘   ◘◘◘◘   ◘◘◘◘◘◘")
                print("      ◘    ◘  ◘    ◘  ◘    ◘  ◘    ")
                print("      ◘◘◘◘>   ◘    ◘   ◘◘◘◘   ◘◘◘◘◘◘")
                print("      ◘    ◘  ◘    ◘  ◘    ◘       ◘")
                print("      ◘◘◘◘◘   ◘◘◘◘◘◘  ◘    ◘  ◘◘◘◘◘◘")
                print()
                print(" ◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘◘◘    ◘    ◘◘◘◘◘")
                print(" ◘      ◘      ◘        ◘    ◘   ◘  ◘    ")
                print(" ◘◘◘    ◘◘◘    ◘◘◘◘◘    ◘     ◘◘◘   ◘◘◘◘◘")
                print(" ◘      ◘          ◘    ◘    ◘   ◘      ◘")
                print(" ◘      ◘◘◘◘◘  ◘◘◘◘◘    ◘    ◘   ◘  ◘◘◘◘◘")
                print()

        case 2:
            print("Então não vale a pena estar aqui. ADEUS")
        case 3:
            print()
            
            


         

    

if __name__ == '__main__':
    main()
