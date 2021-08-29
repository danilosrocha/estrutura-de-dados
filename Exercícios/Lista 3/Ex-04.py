class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def print_deque(self):
        print(self.items)

    def search(self, item):
        cont = 0
        for i in range(0, len(self.items)):
            if self.items[i] == item:
                cont += 1
                break        

d = Deque()
final = Deque()
l = ""
while l != "X":
    i = input().split()
    l = i[0]
    
    if l == "I": # insere o valor v no início da lista
        d.addRear(i[1])
    elif l == "F": # insere o valor v no final da lista.
        d.addFront(i[1])
    elif l == "D": # remove do início e imprime valor removido.
        a = d.removeRear() 
        final.addFront(a) 
    elif l == "P": # remove do final e imprime valor removido.
        a = d.removeFront()
        final.addFront(a)
    elif l == "E": # remove elemento da posição v e retorna o valor removido.
        v = int(i[1]) - 1
        final.addFront(d.items[v])
        d.items.pop(v)
    elif l == "T": # troca o valor da primeira ocorrencia de v pelo valor de n.
        v = i[1]
        n = i[2]
        cont = 0
        for j in range(0, d.size()):
            if d.items[j] == v:
                d.items[j] = i[2]
                break                         
            
while not final.isEmpty():
    print(final.removeRear())

print()
while not d.isEmpty():
    print(d.removeRear())
