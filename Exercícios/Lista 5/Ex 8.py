import math

n = int(input())
comple = []
alt_ideal = 180
peso_ideal = 75

for i in range(n):
        
    lista = []
    carc = input().split()
    nome = carc[0]
    sobre = carc[1]
    alt = int(carc[2])
    peso = int(carc[3])
    sele_alt = math.fabs(alt_ideal - alt)
    sele_peso = math.fabs(peso_ideal - peso)
    lista.append(sele_alt)
    lista.append(sele_peso)
    lista.append(nome)
    lista.append(sobre)
    lista.append(alt)
    lista.append(peso)
    comple.append(lista)
    comple.sort()
    
j = 0
a = 1
while a != len(comple):
    alt_atual = comple[j][4]
    peso_atual = comple[j][5]
    peso = comple[j][5]
    nomei = comple[j][2]
    sobrei = comple[j][3]
    atual_lista = comple[j]

    alt_prox = comple[a][4]
    peso_prox = comple[a][5]
    peso_prox = comple[a][5]
    nome_prox = comple[a][2]
    sobre_prox = comple[a][3]
    prox_lista = comple[a]

    if alt_atual == alt_prox:
        if peso_prox < peso_atual and peso_atual != 75:
            comple.remove(prox_lista)
            comple.insert(j, prox_lista)
    j += 1
    a += 1
    

for i in range(n):
    nomei = comple[i][2]
    sobrei = comple[i][3]
    print(f"{sobrei}, {nomei}")
    