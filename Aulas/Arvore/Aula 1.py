"""class NodoArvore:
    def __init__(self, chave = None, esq = None, dir = None):
        self.chave = chave
        self.esq = esq
        self.dir = dir

    def __str__(self):
        return '%s <- %s -> %s' %(self.esq and self.esq.chave, self.chave, self.dir and self.dir.chave) 


raiz = NodoArvore(40)

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
            
raiz = NodoArvore(40)

for i in [10, 60, 50, 70, 30, 20]:
    inserirABB(raiz, NodoArvore(i))

# Caminhos em árvore
# pré-ordem
    # Raiz, subarvore esq, subarvore dir
# em ordem
    # subarvore esq, raiz, subarvore dir
# pós-ordem
    # subarvore esq, subarvore dir, raiz
# em largura (livro)

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
    print(raiz.chave)"""

""" Pior caso o(n)
Crescente ou descrecente!
[10,20,30,40,50,60]
10
    20
        30
            40
                50
                    60

"""
"""
def maximo(raiz):
    nodo = raiz
    while nodo.dir is not None:
        nodo = nodo.dir
    return nodo.chave

def minimo(raiz):
    nodo = raiz
    while nodo.esq is not None:
        nodo = nodo.esq
    return nodo.chave


print(maximo(raiz))
print(minimo(raiz))
"""

"""# Inserção com listas Livro
def arvore_Bin(r):
    return [r, [], []]

def insertEsq(raiz, novoNo):
    t = raiz.pop(1)
    if len(t) > 1:
        raiz.insert(1, [novoNo, t, []])
    else:
        raiz.insert(1, [novoNo, [], []])
    return raiz

def insertDir(raiz, novoNo):
    t = raiz.pop(2)
    if len(t) > 1:
        raiz.insert(2, [novoNo, [], t])
    else:
        raiz.insert(2, [novoNo, [], []])
    return raiz

minha_arvore = arvore_Bin("A")
insertEsq(minha_arvore, "B")
insertEsq(minha_arvore[1], "D") # Faz com que matenha a ordem dos inseridos
insertEsq(minha_arvore[1][1], "E")
insertDir(minha_arvore, "C")
print(minha_arvore)
"""
    
class Arvore:
    def __init__(self, chave):
        self.chave = chave
        self.dir = None
        self.esq = None
    
    def insEsq(self, novoNo):
        if self.esq == None:
            self.esq = Arvore(novoNo)
        else:
            t = Arvore(novoNo)
            t.esq = self.esq
            self.esq = t
        
    def insDir(self, novoNo):
        if self.dir == None:
            self.dir = Arvore(novoNo)
        else:
            t = Arvore(novoNo)
            t.dir = self.dir
            self.dir = t
    
    def getRightChild(self):
        return self.dir

    def getLeftChild(self):
        return self.esq

    def setRootVal(self, obj):
        self.chave = obj

    def getRootVal(self):
        return self.chave

r = Arvore('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insEsq('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insDir('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
