"""Strings
Cebolinhas as frases

- r -> l
- R -> L
- rr -> ll
- RR -> LL
"""

def cebolinha(frase):
    ultima_letra = False
    nova_frase = ''

    for letra in frase:
        if letra == 'r':
            if not ultima_letra:
                nova_frase += 'l'
            ultima_letra = True
        elif letra == 'R':
            if not ultima_letra:
                nova_frase += 'L'
            ultima_letra = True
        else:
            nova_frase += letra
            ultima_letra = False 
                   
    return nova_frase

def cebolinha2 (frase):
    frase = frase.replace('RR', 'L')
    frase = frase.replace('rr', 'r')
    frase = frase.replace('R', 'L')
    frase = frase.replace('r', 'l')
    
    return frase

# Inicio do programa
frase = input('Escreva uma frase: ')
print(f'O cebolinha diria: {cebolinha2(frase)}')