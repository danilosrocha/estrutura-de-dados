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
    elif nodo.chave > raiz.chave:
        if raiz.dir is None:
            raiz.dir = nodo
        else:
            inserirABB(raiz.dir, nodo)
    else: 
        if raiz.esq is None:
            raiz.esq = nodo
        else:
            inserirABB(raiz.esq, nodo)

def pre_ordem(raiz):
    if not raiz:
        return
    print(raiz.chave)
    em_ordem(raiz.esq)
    em_ordem(raiz.dir)

def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esq)
    print(raiz.chave)
    em_ordem(raiz.dir)

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esq)
    pos_ordem(raiz.dir)
    print(raiz.chave)

comando = int(input())
raiz = NodoArvore(comando)

while comando != "quack":
    comando = input()
    if comando == "in":
        em_ordem()
    elif comando == "pre":
        pre_ordem()
    elif comando == "pos":
        pos_ordem()
    else:
        node = int(comando)
        print(node)
        inserirABB(raiz, node)
