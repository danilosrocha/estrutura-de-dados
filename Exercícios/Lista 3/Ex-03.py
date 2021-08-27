class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
final = Deque()
l = ""
while l != "X":
    i = input().split()
    l = i[0]
    if l == "I": # insere o valor v no início da lista
        d.addFront(i[1])
    elif l == "F": # insere o valor v no final da lista.
        d.addRear(i[1])
    elif l == "D": # remove do início e imprime valor removido.
        a = d.removeFront() 
        final.addFront(a) 
    elif l == "P": # remove do final e imprime valor removido.
        a = d.removeRear()
        final.addFront(a)

while not final.isEmpty():
    print(final.removeRear())

while not d.isEmpty():
    print(d.removeFront())