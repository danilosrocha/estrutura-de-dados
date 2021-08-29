class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        i = 0
        a = 0
        while current != None and not found:
            if current.getData() == item:
                a += 1
            if a == 2:
                found = True  
                return i     
            else:
                current = current.getNext()
            i += 1
       

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        current = self.head
        i = 0
        cont = 0
        while current:
            if current.getData() == item:
                return i
            else:    
                current = current.getNext()
                i += 1

    def get(self, index):
        current = self.head
        for i in range(index):
            if current:
                current = current.getNext()
            else:
                raise IndexError
        if current:
            return current.getData()
        raise IndexError

def removerSegundaOcorrencia(lista, N):
    idx = lista.search(N)
    print(idx)


    



L = UnorderedList()
L.add(42)
L.add(42)
L.add(42)
print(removerSegundaOcorrencia(L, 2))
"""
def removerSegundaOcorrencia(lista, N):
    lista_1 = []
    l = str(lista).split()
    cont = 0
    for i in range(len(l)):
        lista_1.append(int(l[i]))
    for j in range(len(lista_1)):
        if lista_1[j] == N:
            cont += 1
        elif cont == 2:
            lista_1.pop(j-1)
            break
    
    
    
    #l.append("")
    #for i in range(len(l) - 1):
        #if l[i] == l[i+1]:
            #print("repetido")
    
    #for i in range(0, len(lista)):
        #print(lista.head[i])
"""