import math

dados = int(input())

print(f'Transmitindo {dados} bytes...')

seg = 0
cont_parcial = 0
cont_total = 0
for i in range (dados*dados):
    seg += 1
    bytes = int(input()) 
    cont_parcial += bytes
    cont_total += bytes
    if seg == 5: # A cada 5 segundos
        taxa_seg = cont_parcial / 5
        if cont_parcial == 0:
            print('Tempo restante: pendente...')
        else:
            tempo_rest = math.ceil(float(f'{(dados - cont_total) / taxa_seg:.2f}'))
            if tempo_rest != 0:
                print(f'Tempo restante: {tempo_rest} segundos.')
        seg = 0
        cont_parcial = 0
    if cont_total >= dados:
        break

print(f'Tempo total: {i + 1} segundos.')
