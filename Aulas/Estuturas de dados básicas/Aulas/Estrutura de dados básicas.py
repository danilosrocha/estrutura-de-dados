
'''
4     <- Topo da pilha
3
2 <- Remover o elemento 
1
----  <- Base da pilha
'''

#Tipo Abstrato de Dados -> TAD

#from pythonds.basic import Stack
#s = Stack()
#s.pop()

#Quais são as TADs da Pilha?

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

#imprimir a palavra "ED2021/1"
'''
p = Pilha()
print('Pilha vazia:', p.isEmpty())
#push
p.push('1')
p.push('/')
p.push('1')
p.push('2')
p.push('0')
p.push('2')
p.push('D')
p.push('E')
print('Último elemento inserido', p.peek())
print('Tamanho da Pilha', p.size())

#pop?
while not p.isEmpty():
  print(p.pop(), end='')
print()
'''

'''
Escrever um função palindromo que verifica se a palavra é palíndromo.

Entrada => saída
Ex1 print(palindromo('arara')) => True
Ex2 print(palindromo('123321)) => True
Ex3 print(palindromo('12332))  => False
Ex4 print(palindromo('1221))   => True
'''

#Qual seria a lógica?

def palindromo(pal):
  p = Pilha()
  i = 0
#Empilhar pal//2 string
  while i < len(pal)//2:
    p.push(pal[i])
    i += 1
#Descartar o elemento central caso o tamanho da string seja impar
  if len(pal)%2 != 0:
    i = i + 1
#Comparar topo da pilha com a proxima letra
  while not(p.isEmpty()):
#  Se as letras são iguais, desempilhar
    if p.peek() == pal[i]:
      p.pop()
      i += 1
    else: 
      return False
  return True
#  Se não, não é palíndromo

#print(palindromo('arara'))
#print(palindromo('123321'))
#print(palindromo('12332'))
#print(palindromo('1221'))



'''
Escreva um programa que dado um numero inteiro (i>=0) na entrada, converte esse número decimal para binário usando Pilha. Imprimir na tela.

Entrada => Saída
Ex1. 6 => 110
Ex2. 15 => 1111
Ex2. 2 => 10
'''

decimal = int(input())
p = Pilha() 

while decimal >= 0:
  resto = decimal%2
  p.push(resto)
  decimal = decimal//2
  if decimal == 0:
    break

#binario = ''
#binario2 = []
#Desempilhar
while not p.isEmpty():
  #binario2.append(p.pop())
  print(p.pop(), end = '')

print()
#print(*binario2, sep='')


