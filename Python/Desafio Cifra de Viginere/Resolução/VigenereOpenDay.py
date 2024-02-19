# VIGENÈRE CYPHER
#
def encrypt( msg, key ):
    ''' ( str, str ) -> str

    encrypts a message with the vigenère cypher using key
    '''
    result = ''
    i = 0
    
    for c in msg:       
        r = ord( c ) + ord( key[i] ) - ord( 'a' ) + 1       

        if r > ord( 'z' ):
            r = r - 26
            
        result = result + chr( r )
        
        i = i + 1
        if i == len( key ):
            i = 0
        
    return result
    
def decrypt( code, key ):
    ''' ( str, str ) -> str

    decrypts a cypher text with the vigenère cypher using key
    '''
    result = ''
    i = 0
    for c in code:
        r = ord( c ) - ord( key[i] ) + ord( 'a' ) - 1

        if r < ord( 'a' ):
            r = r + 26
            
        result = result + chr( r )

        i = i + 1
        if i == len( key ):
            i = 0
        
    return result

# main function
def main():

    encryptedMessage = ''
    
    cifraf = open('cifra.txt', 'r')
    lines = cifraf.readlines()

    for line in lines:
        encryptedMessage += line
    
    print("Cifra: ", encryptedMessage)

    palavraf = open('palavras.txt', 'r')
    lines = palavraf.readlines()

    for palavra in lines:
        palavra = palavra.strip() # eliminates newline in the end
        decryptedText = decrypt( encryptedMessage, palavra )
        print( '\n' + 'Key: ', palavra, '\nDecrypted Message : ' + decryptedText + '\n' )
        option = input( "Is this a readable text? (Y)es or (N)o  ")
        if option == 'Y' or option == 'y':
            message = decryptedText
            break
        
    PIN = message[len(message)-2:len(message)]
    print( "\nPIN:", ord(PIN[0]), end='' )
    print( ord(PIN[1]) )

if __name__ == '__main__':
    main()
