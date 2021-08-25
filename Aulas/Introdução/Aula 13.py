"""frase = 'Olá pessoal, tudo certo?'
print (frase[0:8] + frase[8:len(frase)]) 

print (frase[::-1]) #percorre a string ao contrario
"""
"""String
Cadeia de caracteres
"""
def palindromo_string(frase):
    return frase == frase[::-1]

def palindromo(frase):
    frase = frase.replace(' ', '')
    return frase.lower() == frase[::-1].lower()

def busca_string(frase, string):
    cont = 0
    i = -1
    while True:
        i = frase.find(string, i + 1 )
        if i == -1:
            return cont
        else:
            cont += 1

def busca_palavra(frase, palavra):
    letras_validas = 'abcdefghijklmnopqrstuvwxyv'
    cont = 0
    palavra_aux = ''

    for letra in frase:
        if letra.lower() in letras_validas:
            palavra_aux += letra 
        else:
            if palavra_aux.lower() == palavra.lower():
                cont += 1
            palavra_aux = ''
    return cont
    

#Inicio do programa
frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')
print(f'É uma palavra palindromo? {palindromo_string(frase)}')
print(f'É uma frase palindromo? {palindromo(frase)}')
print(f'Possui {busca_string(frase, palavra)} ocorrencias da strinh {palavra}')
print(f'Possui {busca_palavra(frase, palavra)} ocorrencias da palavra {palavra}')