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

n, f, p = map(int, input().split())
# n: indicando a quantidade de veículos/ f: o fator de amostragem/ p: limite de peso 
lista = Deque()
kg = input().split()
t1 = 1
t2 = 5
t3 = 10
tf = 0
i = 0
livre = abs(f - n + 1)
for i in range(0, n, f):
    m = int(kg[i]) # percorrer o deque
    lista.addFront(m)
    tam = lista.size() 
    if m <= p:
        tf += t2
    else:
        tf += t3 
        p = m - 2
        if f == 1:
            tf += t2

if f != 1:     
    if i != 0:
        espaços = livre * i
        while espaços > 0:
            espaços -= 1
            tf += 1
    else:
        espaços = livre * 1
        o = espaços // n
        while o > 0:
            o -= 1
            tf += 1
        

print(tf)
