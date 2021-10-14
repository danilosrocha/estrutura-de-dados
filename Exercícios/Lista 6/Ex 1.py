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

def nivel(raiz, n):
   nodo = raiz
   altEsq = -1
   altDir = -1
   print(nodo.esq)
   print(nodo.dir)
   if nodo.esq:
      print(nodo.esq)
      if nodo.esq == n:
         return altEsq + 1  
      else:
         altEsq = nivel(nodo.esq, n)
         return altDir + 1  
   if nodo.dir:
      print(nodo.dir)
      if nodo.dir == n:
         return altDir + 1  
      else:
         altDir = nivel(nodo.dir, n)
         return altDir + 1 
   return altDir + 1  

raiz = NodoArvore(40)
for i in [10, 60, 50, 70, 30, 20]:
    inserirABB(raiz, NodoArvore(i))

print(nivel(raiz, 60))

   