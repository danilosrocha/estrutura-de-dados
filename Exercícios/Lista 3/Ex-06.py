class Pilha:
  def __init__(self):
    self.itens = []

  def isEmpty(self):
    return self.itens == []

  def pop(self):
    return self.itens.pop()

  def push(self, item):
    self.itens.append(item) 

  def peek(self):
    return self.itens[-1]
 
  def size(self):
    return len(self.itens)

  def clear(self):
    self.itens = []

n = int(input())
roupas = Pilha()
cores = Pilha()
total = 0

for i in range(n):
    peca, cor, tempo = input().split()
    t = int(tempo)
    total += t
    roupas.push(peca)
    cores.push(cor)

while not roupas.isEmpty():
    print("Tipo:", roupas.pop(), end = ", ")
    print("Cor:", cores.pop(), end = "\n" )

print(f"Total de roupas: {n}")
print(f"Total de tempo: {total}")