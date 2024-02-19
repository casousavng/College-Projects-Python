import time

def temporizador(tempo):
    while tempo:
        mins, segs = divmod(tempo, 60)
        formato = "{:2d} seg...".format(segs)
        print(formato, end='')
        time.sleep(1)
        tempo -= 1

def arvore3andar(a):
    for i in range(a-2):
        for b in range(a-i):
            print(" ", end=" ")
        for c in range(2*i+1):
            print("◉",end=" ")
        print()
        
def arvore2andar(a):
    for i in range(a-1):
        for b in range(a-i):
            print(" ", end=" ")
        for c in range(2*i+1):
            print("◉",end=" ")
        print()
        
def arvore1andar(a):
    for i in range(a):
        for b in range(a-i):
            print(" ", end=" ")
        for c in range(2*i+1):
            print("◉",end=" ")
        print()
                
def tronco(a):
    for i in range(a-2):
        for b in range(a-1):
            print(" ", end=' ')
        print("|◼◼◼︎︎|")
    print()

def embrulhoAberto():
        print()
        print(" \\                              //")        
        print("  \\                            //")
        print("   \\                          // ")     
        print("    \\                        //  ")
        print("    ***************************")
        print("    ***************************")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    *+++++++++++++++++++++++++*")
        print("    *       A Abrir......     *")
        print("    *         AGUARDE         *")
        print("    *+++++++++++++++++++++++++*")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    ***************************")
        print("    ***************************")
        print()

def embrulhoFechado():
        print()
        print("               V    V       ")
        print("                V  V        ")
        print("                 WW         ")
        print("    ***************************")
        print("    ***************************")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    *+++++++++++++++++++++++++*")
        print("    *      AQUI ESTA ELE      *")
        print("    *        :) :) :)         *")
        print("    *+++++++++++++++++++++++++*")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    **           ||          **")
        print("    ***************************")
        print("    ***************************")
        print()

def mensagem():
        print()
        print("              UM POSTAL ONDE LHE DESEJO OS VOTOS        ")
        print()
        print(" 🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄")
        print(" 🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄")
        print("🎄🎄                                                   🎄🎄")
        print("🎄🎄                                                   🎄🎄")
        print("🎄🎄           ◘◘◘◘◘   ◘◘◘◘◘◘   ◘◘◘◘   ◘◘◘◘◘◘          🎄🎄")
        print("🎄🎄           ◘    ◘  ◘    ◘  ◘    ◘  ◘               🎄🎄")
        print("🎄🎄           ◘◘◘◘>   ◘    ◘   ◘◘◘◘   ◘◘◘◘◘◘          🎄🎄")
        print("🎄🎄           ◘    ◘  ◘    ◘  ◘    ◘       ◘          🎄🎄")
        print("🎄🎄           ◘◘◘◘◘   ◘◘◘◘◘◘  ◘    ◘  ◘◘◘◘◘◘          🎄🎄")
        print("🎄🎄                                                   🎄🎄")
        print("🎄🎄      ◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘◘◘    ◘    ◘◘◘◘◘     🎄🎄")
        print("🎄🎄      ◘      ◘      ◘        ◘    ◘   ◘  ◘         🎄🎄")
        print("🎄🎄      ◘◘◘    ◘◘◘    ◘◘◘◘◘    ◘     ◘◘◘   ◘◘◘◘◘     🎄🎄")
        print("🎄🎄      ◘      ◘          ◘    ◘    ◘   ◘      ◘     🎄🎄")
        print("🎄🎄      ◘      ◘◘◘◘◘  ◘◘◘◘◘    ◘    ◘   ◘  ◘◘◘◘◘     🎄🎄")
        print("🎄🎄                                                   🎄🎄")
        print("🎄🎄                                                   🎄🎄")
        print(" 🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄")
        print(" 🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄")
        print()
        print("Aluno: Carlos André Sousa\nAno: 2022/2023")

def main():
    
    print()
    print("###############################################################################")
    print("#                                                                             #")
    print("#  Chegamos a uma das mais belas alturas do ano, o NATAL, e com ele vem       #")
    print("#  a reuniao da familia e dos amigos, a docaria tipica, as luzes coloridas    #")
    print("#  os presepios, os enfeites variados, a arvore de natal, os presentes, etc.  #")
    print("#                                                                             #")
    print("###############################################################################")
    print()
    print("Tenho um presente para si, mas preciso de uma arvore para o colocar.")
    print("--------------------------------------------------------------------")
    print()
    print("Vamos contruir uma arvore de natal.")
    print()
    print("Prefere um arvore:")
    print(" 1 - Pequena ")
    print(" 2 - Media ")
    print(" 3 - Grande ")
    
    tamanho = int(input('A sua escolha: '))
    while tamanho < 1 or tamanho > 3:
        tamanho = int(input("Opção Incorreta! Escolha uma opçao entre 1 e 3: "))
    print()

    match tamanho:
      
      case 1:
        altura = int(input("Qual a altura da arvore pretendida (entre 4 e 10 por favor) \ne tenha em atenção que este valor não inclui o tronco: "))
        print()
        while altura < 4 or altura >10:
            altura = int(input("Altura Incorreta! Escolha apenas valores entre 4 e 10: "))
            print()
        arvore1andar(altura)
        tronco(altura)
            
      case 2:
        altura = int(input("Qual a altura da base da arvore pretendida (entre 4 e 10) e não inclui o tronco: "))
        print()
        while altura < 4 or altura >10:
            altura = int(input("Altura Incorreta! Escolha apenas valores entre 4 e 10: "))
            print()
        arvore2andar(altura)
        arvore1andar(altura)
        tronco(altura)
        
      case 3:
        altura = int(input("Qual a altura da base da arvore pretendida (entre 4 e 10) e não inclui o tronco: "))
        print()
        while altura < 4 or altura >10:
            altura = int(input("Altura incorreta! Escolha apenas valores entre 4 e 10: "))
            print()
        arvore3andar(altura)
        arvore2andar(altura)
        arvore1andar(altura)
        tronco(altura)


    print("##############################################################################")
    print("#                                                                            #")
    print("#                                MUITO BEM !                                 #")
    print("#    Agora que temos uma arvore chegou a altura de colocar la o presente.    #")
    print("#                                                                            #")
    print("##############################################################################")
    print()
    print()
    print("Presente a aparecer em: ", end='')
    temporizador(3)
    print()
    embrulhoFechado()

    while True:
        print()
        presente = input("VAMOS ABRIR ??? até eu quero saber o que é :)\nDigite 'Sim' para abrir ou 'Nao' se não quiser abrir já: ")
        if presente == "SIM" or presente == "sim" or presente == "Sim":
            print()
            embrulhoAberto()
            print()
            print("Presente a abrir em: ", end='')
            temporizador(3)
            print()
            print()
            mensagem()
            break
        else:
            print()
            print("OK, entao abra só quando quiser :(")
            print("Obrigado e volte quando realmente quiser saber o que é.")
            break

if __name__ == '__main__':
    main()
