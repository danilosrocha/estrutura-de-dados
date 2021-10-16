RAIZ = " "
class Fila:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class Arvore:
    def __init__(self, raiz):
        self.chave = raiz
        self.esq = None
        self.dir = None

    def __str__(self):
        return '%s' %(self.chave) 
         
    def insertEsq(self, novoNo):
        if self.esq == None:
            self.esq = Arvore("*")
        else:
            t = Arvore(novoNo)
            t.esq = self.esq
            self.esq = t

    def insertDir(self, novoNo):
        if self.dir == None:
            self.dir = Arvore(novoNo)
        else:
            t = Arvore(novoNo)
            t.dir = self.dir
            self.dir = t
    
    def em_altura(self, node = RAIZ):
        if node == RAIZ:
            node = self.chave
        
        fila = Fila()
        fila.enqueue(node)
        while not fila.isEmpty():
            node = fila.dequeue()
            print(node, end = " ")
            if node.esq:
                fila.enqueue(node.esq)
            if node.dir:
                fila.enqueue(node.dir)
    
    def getDir(self):
        return self.dir

    def getEsq(self):
        return self.esq

    def setRaiz(self, obj):
        self.chave = obj

    def getRaizVal(self):
        return self.chave


numeros = int(input())
dicionario1 = {}
dicionario2 = {}
lista = []
Lista_mensagem = []
for cont in range(numeros):
    comando = input().split()
    letra = comando[0]
    codigo = comando[1]
    dicionario1.update({letra:codigo})
    dicionario2.update({codigo:letra})

mensagem = int(input())

if mensagem == 1:
    mensagem = input()
    for letras in mensagem:
        if letras == " ":
            lista.append("/")
            if lista[-2] != "/":
                Lista_mensagem.append("/")
        else:
            if letras in dicionario1:
                lista.append(dicionario1[letras])
                Lista_mensagem.append(dicionario1[letras])
                Lista_mensagem.append(" ")
            else: 
                print("Impossível codificar a mensagem!")
                exit()
    print(*Lista_mensagem, sep = "")

elif mensagem == 0:
    mensagem = input().split()

    espaço = "/"
    for codigo in mensagem:
        if espaço in codigo:
            Lista_mensagem.append(" ")
            Lista_mensagem.append(dicionario2[codigo[1:]])
        else:
            if codigo in dicionario2:
                Lista_mensagem.append(dicionario2[codigo])
            else:
                print("Impossível decodificar a mensagem!")
                exit()
    print("".join(Lista_mensagem))

mA = Arvore("*")

for codigo, letra in dicionario2.items():
    #for analise in codigo:
    if codigo[0] == ".":
        mA.insertEsq(letra)
    elif codigo[0] == "-":
        mA.insertEsq(letra)

mA.em_altura(mA)

""" Teste
5
A .
C -
R .-
T ..
! -.
0
. .. . - . .- -.

"""