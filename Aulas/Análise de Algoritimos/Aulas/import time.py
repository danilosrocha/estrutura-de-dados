import time

def soma_ate(n):
    resultado = 0                  # linha 1
    for i in range(1, n + 1):      # linha 2
        resultado = resultado + i  # linha 3
    return resultado 
num_testes = 5

media = 0

for _ in range(num_testes):
    inicio = time.time()
    soma_ate(1000000000)
    fim = time.time()
    
    tempo_de_execucao = fim - inicio
    media += tempo_de_execucao
    print(f'Tempo: {tempo_de_execucao}')

media /= num_testes
print(f'Média de tempo: {media}') 