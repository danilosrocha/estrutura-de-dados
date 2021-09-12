dicionario = {0: 0}

def fib(n):
    if n in dicionario:
        dicionario[n] += 1
    else:
        dicionario[n] = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input())
print(f"fibonacci({n}) = {fib(n)}.")

for elem, quant in sorted(dicionario.items()):
    print(f"{quant} chamada(s) a fibonacci({elem}).")

    

    