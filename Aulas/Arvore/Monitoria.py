class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def __str__(self):
        return str(self.chave)

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

def mostra(raiz, pref):
    print(f"{pref}", end ="")
    if raiz:
        print(raiz.dado, end = "")
        print(" ", end ="")
        mostra(raiz.esq)
        print(" ", end ="")
        mostra(raiz.dir)
    print(")", end ="") 