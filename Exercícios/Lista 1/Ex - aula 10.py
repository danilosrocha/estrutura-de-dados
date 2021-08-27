""""Iteração com While

Calculadora:
raiz quadrada
raiz cubica
seuquencia de fib

"""

def escolheOperacao():
    print('Operacoes:')
    print('1- Raiz quadrada')
    print('2- Raiz cubica')
    print('3- Fibonacci')
    ope = int(input('Escolha a operacao: '))
    return ope

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        n1 = 0
        n2 = 1
        i = 2
        while i <= num:
            res = n1 + n2
            n1 = n2
            n2 = res
            i += 1
        return res

ope = escolheOperacao()
num = int(input('Digite um numero inteiro: '))
if ope == 3:
    print(f'O {num} de Fibonacci é {fib(num)}')