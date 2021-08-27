# sequencia = []
# sequencia.append(7)

class Pilha:
  #Criar um construtor
  def __init__(self):
    self.itens = []

#isEmpty -> retorna True or False caso a pilha esteja vazia
  def isEmpty(self):
    return self.itens == []
    #len(self.itens) == 0

#pop -> Retorna e remove o elemento que está no topo da Pilha
  def pop(self):
    return self.itens.pop()

#push -> adiciona um elemento na Pilha
  def push(self, item):
    self.itens.append(item) 

#peek -> olhar o topo da pilha, sem remover o valor
  def peek(self):
    return self.itens[-1]
    #return self.itens[len(self.itens)-1]

#size -> retorna o tamanho da pilha
  def size(self):
    return len(self.itens)

#clear -> remove todos os elementos da pilha
  def clear(self):
    self.itens = []


"""p = Pilha()

n = 8
for i in range(n):
  ele = input()
  p.push(ele)
print('Último elemento inserido', p.peek())
print('Tamanho da Pilha', p.size())
print('Pilha Vazia:', p.isEmpty())

#pop?
while not p.isEmpty():
  print(p.pop(), end = '')

print()
print('Pilha vazia:', p.isEmpty())
"""

"""def palindromo(pal):
  p = Pilha()
  i = 0
#Empilhar pal//2 string
  while i < len(pal)//2:
    p.push(pal[i])
    i += 1
#Descartar o elemento central caso o tamanho da string seja impar
  if len(pal)%2 != 0:
    i += 1
#Comparar topo da pilha com a proxima letra
  while not(p.isEmpty()):
#  Se as letras são iguais, desempilhar
    if p.peek() == pal[i]:
      p.pop()
      i += 1
    else: 
      return False
  return True

print(palindromo('arara'))
"""

decimal = int(input())
p = Pilha() 

while decimal >= 0:
  resto = decimal%2
  p.push(resto)
  decimal = decimal//2
  if decimal == 0:
    break
  
#Desempilhar
while not p.isEmpty():
  #binario2.append(p.pop())
  print(p.pop(), end = '')

print()