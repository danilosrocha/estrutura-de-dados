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

n = int(input())
tem = 'A expressão possui duplicata.'
nao_tem = 'A expressão não possui duplicata.'
f = Fila()

for i in range(n):
    seq = input()
    d = 0
    tamanho = 0
    for j in range(len(seq)):
        if seq[j] == '(' :
            d += 1
            if d == 2:
                f.enqueue(tem)
                d = 0
                tamanho = f.size()
                break
        elif seq[j] == ')':
            d = 0
    if tamanho == 0:
        f.enqueue(nao_tem)
        tamanho = 0

    

while not f.isEmpty():
    print(f.dequeue(), end = "\n")
"""for i in range(n):
    seq = input()
    d = 0
    for j in range(len(seq)):
        if seq[j] == '(':
            d += 1
        elif seq[j] == '/' and d == 2:


            if d == 2:
                f.enqueue(tem)
                d = 0
                break
        else:
            f.enqueue(nao_tem)
            break
    
while not f.isEmpty():
    print(f.dequeue(), end = "\n")
"""
            

    
            
   