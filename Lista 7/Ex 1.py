def nivel(raiz, n):
    nodo = raiz
    if nodo == None:
        return -1
    altEsq = -1
    altDir = -1
    if nodo.esq != n and nodo.esq != None:
        print(altEsq)
        altEsq = nivel(nodo.esq, n)
    if nodo.dir != n and nodo.dir != None:
        print(altDir)
       altDir = nivel(nodo.dir, n)
    
    
    if altDir > altEsq:
        return altDir + 1
    return altEsq + 1