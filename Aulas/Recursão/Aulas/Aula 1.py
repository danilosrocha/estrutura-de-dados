"""
Três pontos:
--> Caso Base
--> Modificar o seu estado para se aproximar do caso base
--> Chamar a função
"""

# Ex 1 -> Somatório recursivo de numeros naturais

"""
def soma_nat(n):
    global cont
    #caso base:
    if n == 0:
        return 0
    else:
        cont += 1
        return n + soma_nat(n - 1)

cont = 0
print(soma_nat(1))
print(cont)

"""

# Ex 2 -> Função recursiva que devolve como resultado a divisão de m por n
"""
def div(dividendo, divisor):
    # Caso base
    # dividendo < divisor
    if dividendo < divisor:
        return 0
    # Caso geral
    # dividendo >= divisor
    # Quociente é a quantidade de vezes que se pode subtrair o dividendo pelo divisor
    else:
        return 1 + div(dividendo - divisor, divisor)

print(div(20,5))

"""

# Ex 3 -> Função copmprimento que calcula o comprimento de uma lista:
"""
def comp(l):
    # Caso base
    if l == []:
        return 0
    # Caso geral
    else:
        return 1 + comp(l[1:])

print(comp([1, 2, 3, 4, 5]))

"""

# Ex 4 -> Funcao recursiva que calcula valor medio de uma lista
"""
def somalista(l):
    if l == []:
        return 0
    else:
        
        return l[0] + somalista(l[1:])

def media(l):
    return somalista(l)/len(l)
print(media([1, 1, 1, 1]))

"""

# Ex 5 -> Funcao recursiva ate que devolva a lista dos numeros naturais ate um valor dado n

def ate(n):
    if n == 0:
        return []
    else:
        return ate(n - 1) + [n - 1] 

print(ate(1))


# Ex 6 -> Funcao recursiva palindromo
"""
def palindromo(seq):
    if len(seq) < 2: #Caso base
        return True
    elif seq[0] != seq[-1]:
        return False
    else:
        return palindromo(seq[1:len(seq) - 1])
    
print(palindromo("dannad"))

"""

# Ex 7 -> Funcao recursiva que retorna o valor max da lista de numeros
"""
def maxList(l):
    if l == []:
        return -1   
    elif len(l) == 1:
        return l[0]
    elif l[0] > maxList(l[1:]):
        return l[0]
    else:
        return maxList(l[1:])

print(maxList([1, 2, 3, 4]))

"""

# Ex 8 -> Funcao recursiva Fatorial
"""
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(1))
"""

# Ex 9 -> Funcao recursiva Fibo

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
