def main():


    
    print("$ DICIONARIO DE PAISES E RESPETIVAS CAPITAIS $")


    #novo = input("Adicionar novo pais: ")

    novo = 0
    
    
    while novo != "nao":

        novo = input("Adicionar novo pais: ")

        
        capital = input("Qual a capital: ")
    
        capitais = { "Portugal": "Lisboa",
                 " Brasil" : "Brasilia",
                 "Espanha" : "Madrid",
                 "França"  : "Paris"   }

        capitais[novo] = capital

        pais = input("Qual o nome do pais? ")

        print("A capital de", pais, "é", capitais.get(pais))
        

        

    print("Obrigado")

    #continuar = input(print("Pretende continuar? (SIM/NAO)"))

        





    

    














if __name__ == '__main__':
    main()
