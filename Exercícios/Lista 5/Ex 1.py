n = int(input())
tudo = []
for i in range(n):
    lista = []
    nome = input()
    t1, t2, t3 = map(float, input().split())
    total = (t1 + t2 + t3) 
    hora = total // 60
    minu = total - hora * 60
    if minu < 10:
        tempo = str(int(hora)) + ":" + "0" + str(f'{minu:.3f}')
    else:
        tempo = str(int(hora)) + ":" + str(f'{minu:.3f}')
    lista.append(tempo)
    lista.append(nome)
    tudo.append(lista)
    tudo.sort()


for i in range(n):
    nomei = tudo[i][1]
    tempoi = tudo[i][0]
    print(f"{i + 1}. {nomei} ({tempoi})")
    
    
   
