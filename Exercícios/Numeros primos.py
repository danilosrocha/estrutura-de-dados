"""Divisores Primos
Números primos gêmeos são pares de números primos (p1, p2) tais que p2=p1+2.

Implemente uma função chamada primos_gemeos que recebe um número inteiro n e retorna os n primeiros pares de números primos gêmeos, conforme formatação indicada abaixo.

Entrada:
Um número inteiro 0≤ n ≤80.

Saída da Função:
Uma lista com os n primeiros pares de números primos gêmeos, sendo cada par definido em uma tupla.

Observações: Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.

O que faz um número ser primo:
Ser divisível por ele mesmo e por 1

"""

# Funcao que recebe a quantidade de pares e imprime de dois em dois seguido do anterior
def primos_gemeos (n):
    p1 = 3 # parte que identifica os numeros primos
    primo = []
    i = 0
    for i in range(n*n):
        p2 = p1 + 2
        cont = 0
        cont2 = 0
        for j in range (1, p2 + 1):
            if p1 % j == 0:
                cont += 1
            if p2 % j == 0:
                cont2 += 1    
        if cont <= 2 and cont2 <= 2:      
            primo.append((p1, p2))
            if len(primo) == n:
                break
        p1 = p2
    return primo
 
n = int(input())
print (primos_gemeos(n))


    