def notas():
    n = int(input())
    lista = []
    if n % 2 != 0 and n > 2:
        for i in range(n):
            numeros = float(input())
            lista.append(f"{numeros:.2f}")
        lista_organizada = sorted(lista)
        print(lista_organizada[0])
        print(lista_organizada[n//2])
        print(lista_organizada[-1])        

    else:
        return(notas())
notas()
