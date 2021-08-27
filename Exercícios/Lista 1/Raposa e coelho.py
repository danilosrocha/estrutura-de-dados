n = int(input())

# Colocar as coordenadas do coelho e da raposa
coelho_x, coelho_y  = map(float, input().split())

raposa_x, raposa_y = map(float, input().split())

b = 0

for i in range(n):
    buraco_x, buraco_y = map(float, input().split())

    coelho_dist = (((coelho_x - buraco_x) ** 2) + ((coelho_y - buraco_y) ** 2)) ** 0.5

    raposa_dist = (((raposa_x - buraco_x) ** 2) + ((raposa_y - buraco_y) ** 2)) ** 0.5
    
    if (2 * coelho_dist) < raposa_dist:
        print(f'O coelho pode escapar pelo buraco ({buraco_x:.3f}, {buraco_y:.3f})')
        break
    b += 2
else:
    print('O coelho nao pode escapar.')

