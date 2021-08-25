n = int(input())  
seg_atual = 0
cont = 0
for i in range(n):
    zero = input()
    for j in range(len(zero)):
        seg_anterior = seg_atual
        if zero[j] == '1': # Procura pelo 1
            seg_atual = j
            a = (seg_atual - seg_anterior) - 1
            if a >= 0:
                cont += a
    print(cont)
    cont = 0
           