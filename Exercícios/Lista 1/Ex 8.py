n = int(input())
letras = []
numeros = []
resultado = ''
num = ''
for i in range(n):
    seq = input() 
    for i in range(len(seq) + 1):
        char = seq + 'A'
        if char[i] in 'ABCDEFGHIJKLMNOQRSTUVWXYZ':
            letras.append(char[i])
            if num != '':
                numeros.append(int(num))
                num = ''
        else:
            num += char[i]
    a = ''
    parcial = ''
    for j in range(len(numeros)):
        resultado += letras[j] * numeros [j]

    print(resultado)
    resultado = ''  
    letras = []
    numeros = []


    
    
        