class NodoArvore:
    def __init__(self, chave = None, esq = None, dir = None):
        self.chave = chave
        self.esq = esq
        self.dir = dir
    
    def __str__(self):
        return '%s' %(self.chave) 

def inserirABB(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif nodo.chave > raiz.chave: #Valor vai p/ direita pq é maior que a raiz
        if raiz.dir is None:
            raiz.dir = nodo # Valor 
        else:
            inserirABB(raiz.dir, nodo)
    else: 
        if raiz.esq is None:
            raiz.esq = nodo
        else:
            inserirABB(raiz.esq, nodo)

def altura(raiz):
    nodo = raiz
    altEsq = -1
    altDir = -1
    if nodo.esq:
       altEsq = altura(nodo.esq)
    if nodo.dir:
       altDir = altura(nodo.dir)
    if altDir > altEsq:
        return altDir + 1
    return altEsq + 1
    
n = int(input())

a = input().split()

raiz = NodoArvore(int(a[0]))
for i in range(1, n):
    nodo = int(a[i])
    inserirABB(raiz, NodoArvore(nodo))

print(altura(raiz))
