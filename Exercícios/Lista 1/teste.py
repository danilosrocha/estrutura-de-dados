n = int(input()) # 

for i in range(n):
    zero = input()
    estado = 0
    aux = 0
    for j in range(len(zero)):
        if zero[j] == '1':
            print(f'{j}: Achei um 1 aqui')