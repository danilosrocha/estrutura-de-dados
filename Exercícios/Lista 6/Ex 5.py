class NodoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
    
    def __str__(self):
        return str(self.chave)

    def pre_ordem(self, node=None):
        if node is None:
            node = self.root
        print(node, end="")
        if node.esq:
            print(" ", end = "")
            self.pre_ordem(node.esq)
        if node.dir:
            print(" ", end = "")
            self.pre_ordem(node.dir)

    def pos_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.esq:
            self.pos_ordem(node.esq)
            print(" ", end = "")
        if node.dir:
            self.pos_ordem(node.dir)
            print(" ", end = "")
        print(node, end="")


    def em_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.esq:
            self.em_ordem(node.esq)
            print(" ", end = "")
        print(node, end="")
        if node.dir:
            print(" ", end = "")
            self.em_ordem(node.dir)
            

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

            


inicial = input()
num = inicial.isdigit()

while num != True:
    print()
    inicial = input()
    num = inicial.isdigit()

base = int(inicial)
raiz = NodoArvore(base)

comando = " "
while comando != "quack":
    comando = input()
    num = comando.isdigit()
    if comando == "pre":
        raiz.pre_ordem(raiz)
        print()
    elif comando == "pos":
        raiz.pos_ordem(raiz)
        print()
    elif comando == "in":
        raiz.em_ordem(raiz)
        print()
    elif num == True:
        node = int(comando)
        inserirABB(raiz, NodoArvore(node))
