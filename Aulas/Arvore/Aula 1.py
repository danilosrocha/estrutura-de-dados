class NodoArvore:
    def __init__(self, chave = None, esq = None, dir = None):
        self.chave = chave
        self.esq = esq
        self.dir = dir

    def __str__(self) -> str:
        return "%s <-- %s --> %s" %(self.esq, self.chave, self.dir) 

def inserirABB(raiz, nodo):
    if raiz is None:
        raiz = nodo

    elif nodo.chave > raiz.chave: #Valor vai p/ direita pq é maior que a raiz
        if raiz.dir is None:
            raiz.dir = nodo
        else:
            inserirABB(raiz.dir, nodo)

    else: 
        if raiz.esq is None:
            raiz.esq = nodo
        else:
            inserirABB(raiz.esq, nodo)
            
raiz = NodoArvore(40)
l = [10, 60, 50, 70, 30, 20]

for i in l:
    inserirABB(raiz, NodoArvore(i))

print(raiz)

    