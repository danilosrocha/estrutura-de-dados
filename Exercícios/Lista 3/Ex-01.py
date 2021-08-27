class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_font(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



def exibe_candidatos(deque, pos, ordem):
    if deque.is_empty():
        return
    else:   
        a = deque.size()
        i = 0
        if ordem == 'direta':
            while i < pos:
                deque.remove_front()
                i += 1
            while not deque.is_empty():
                print(deque.remove_front())
        else:
            while a > pos + 1:
                deque.remove_rear()
                a -= 1
            while not deque.is_empty():
                print(deque.remove_rear())


d = Deque()
exibe_candidatos(d, 2, 'direta')