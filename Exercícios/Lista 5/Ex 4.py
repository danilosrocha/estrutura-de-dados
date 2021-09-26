import operator

n = int(input())
lista = {}
tamanhos = []
#lista = []
for i in range(n):
    nome = input()
    tamanho = len(nome)
    tamanhos.append(tamanho)
    lista.update({tamanho:nome})
    lista_organizada = dict(sorted(lista.items(), reverse = True, key=operator.itemgetter(0)))
tamanhos_organizados = sorted(tamanhos, reverse = True)

j = 0
maior = tamanhos_organizados[0]
while tamanhos_organizados.count(maior) > 1:
    for i in range(tamanhos_organizados.count(maior)):
        tamanhos_organizados.pop(0)
    if len(tamanhos_organizados) != 0:
        maior = tamanhos_organizados[0]
    else: 
        break

if len(tamanhos_organizados) != 0:
    print(lista_organizada[maior])
else:
    print("Que mala suerte!")

