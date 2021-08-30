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
        if self.head == None:
            return
        else:
            current = self.head
            previous = None
            found = False
            a = 0
            while not found:
                if current.getData() == item:
                    a += 1 
                    if a != 2:
                        previous = current
                        current = current.getNext()
                else:
                    previous = current
                    current = current.getNext()
                while a == 2 and not found:
                    found = True
                
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

def removerSegundaOcorrencia(lista, N):
    if lista.search(N) != None:
        lista.remove(N)
    return lista

	
L = UnorderedList()
L.add(42)
L.add(42)
L.add(42)
L = removerSegundaOcorrencia(L, 42)
L = removerSegundaOcorrencia(L, 42)
print(f'Lista: {L}')