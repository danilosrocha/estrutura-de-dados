lista = []

def quadrado_perfeito(n):
    # Caso base
    if n == 1:
        if len(lista) != 0:
            print(f"{n} + soma({lista})")
        else:
            print(f"{n}")
        return 1
    # Caso geral
    else:
        lista.insert(0, n) # Tudo até aqui vai na ida
        x = quadrado_perfeito(n - 2) 
        lista.pop(0) # Tudo a partir daqui vem na volta
        if len(lista) != 0:
            print(f"{n} + soma({lista})")
        else:
            print(f"{n}")

        return x + n
        
n = int(input())

resultado = quadrado_perfeito(2 * n - 1)
print("---------------")
print(f"{n} ** 2 == {resultado}")