"""Defina a função fatorial, que recebe um número e retorna o valor de seu fatorial.
Fatorial (2) = 2 * 1 = 2
Fatorial (3) = 3 * 2 * 1 = 6
Fatorial (n) = n * n-1 * n-2 ... * 1 = 

Entrada
Não há entrada, os casos de teste são definidos para valores inteiros n≥0.

Saída da Função
O valor de n!.

Observações 
Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.

For example:

Test	Result
print(fatorial(0))
1
print(fatorial(1))
1
print(fatorial(3))
6

"""
def fat (n):
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
        print(n)
    return f

n = 4
print (fat(n))
