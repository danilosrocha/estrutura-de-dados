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

    def peek(self):
         return self.items[0]

    def size(self):
        return len(self.items)

player = Deque()
lista_comandos = []
musicas = []
comando = [""]
while comando[0] != "fight":
    comando = input().split()
    if comando[0] == "play" or comando[0] == "add" or comando[0] == "del" or comando[0] == "next":
        lista_comandos.append(comando[0])
    if comando[0] == "play": # começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário).
        pass
    elif comando[0] == "stop": # interrompe a execução da música atual.
        pass
    elif comando[0] == "list": #  mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.
        if player.isEmpty():
            print("[vazia]")
        else:
            if player.size() == 1:
                print(musicas[0], end = '\n')
            else:   
                for i in range(player.size() - 1):
                    print(musicas[i], end = ',')
                print(musicas[-1], end = '\n')             
    elif comando[0] == "current": # mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".
    # Pegará como referencia o play
        if player.isEmpty():
            print("Toque! Toque, Dijê")
        else:
            print(player.peek())
    elif comando[0] == "undo": # desfaz os efeitos de uma instrução add, del, next ou play. Isoladamente, desfaz o efeito da última instrução. Havendo o argumento opcional *, desfaz o efeito de todas as instruções dadas até aquele ponto.
        if len(lista_comandos) != 0 and not player.isEmpty():
            if lista_comandos[-1] == "add":
                player.removeFront()
            elif lista_comandos[-1] == "del":
                pass
            elif lista_comandos[-1] == "next":
                pass
            elif lista_comandos[-1] == "play":
                pass
        if len(comando) >= 2: # Condicao para entrar no undo *
            if comando[1] == "*":
                player = Deque()
    if len(comando) >= 2:
        if comando[0] == "add": # acrescenta a música id ao final da lista.
            player.addFront(comando[1])
            musicas.append(comando[1])
        elif comando[0] == "del": # retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.
            if not player.isEmpty() and comando[1] == musicas[-1]:
                musicas.pop()
                player.removeFront()

        elif comando[0] == "next": # define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de id na lista é realocada para tanto
            if not player.isEmpty() and comando[1] in musicas:
                for i in range(len(musicas)):
                    if musicas[i] == comando[1]:
                        guarda = musicas[1] 
                        musicas[1] = musicas[i] 
                        musicas[i] = guarda
    
print("Jedi Wagner, assuma o comando!")

# Analisar a possibilidade de retirar o Deque
