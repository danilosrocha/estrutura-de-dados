class NodoArvore:
    def __init__(self, chave = None, esq = None, dir = None):
        self.chave = chave
        self.esq = esq
        self.dir = dir

    def __str__(self):
        return '%s <- %s -> %s' %(self.esq and self.esq.chave, self.chave, self.dir and self.dir.chave) 
def inserirABB(raiz, nodo):
    if raiz is None:
        raiz = nodo

    # Verificar o caso base para esq e dir None
    elif nodo.chave > raiz.chave: #Valor vai p/ direita pq é maior que a raiz
        if raiz.dir is None:
            raiz.dir = nodo # Valor 
            print(raiz)
        else:
            inserirABB(raiz.dir, nodo)

    else: 
        if raiz.esq is None:
            raiz.esq = nodo
        else:
            inserirABB(raiz.esq, nodo)

raiz = NodoArvore(1)

for i in [2, 3, 4]:
    inserirABB(raiz, NodoArvore(i))
# A classe ArvoreBinaria já foi definida
def mostra(raiz):
    print("(", end ="")
    if raiz:
        print(raiz.dado, end = "")
        print(" ", end ="")
    if raiz.esq:
        mostra(raiz.esq)
        print(" ", end ="")
    if raiz.dir:
        mostra(raiz.dir)
        print(")", end ="") 
   
print(mostra(1))
