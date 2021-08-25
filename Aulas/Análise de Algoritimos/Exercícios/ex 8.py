Q = [1, 2, 3, 4, 5, 6]
ele = 6
def busca(L, val): 
    achou = False
    comeco = 0
    meio = 0
    fim = len(L) - 1
    while comeco <= fim: 
        meio = (fim + comeco) // 2
        if L[meio] < val: 
            comeco = meio + 1
        elif L[meio] > val: 
            fim = meio - 1
        else:
            achou = True
            return achou, meio 
    return achou, -1

print(busca(Q, ele))