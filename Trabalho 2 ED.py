import operator
RAIZ = "raiz"

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
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None

    def __str__(self):
        return '%s' %(self.chave)

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

