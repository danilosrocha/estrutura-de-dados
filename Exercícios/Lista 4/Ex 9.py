lista = []
n = int(input())
n1 = 0
n2 = 1
cont = 0
fibo = [0, 1]
while len(lista) < n:
    res = n1 + n2
    n1 = n2
    n2 = res
    fibo.append(n2)
    for j in range(fibo[-2], fibo[-1]):
        if j > fibo[-2] and j < fibo[-1]:
            lista.append(j)

if n == 1:
    print(lista[0])
else:
    for i in range(n - 1):
        print(lista[i], end = ', ')
    print(lista[i + 1]) 

