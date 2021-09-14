class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def addPosition(self, i, item):
        self.items.insert(i, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    
    def removePosition(self, i):
        return self.items.pop(i)

    def peek(self):
         return self.items[0]

    def size(self):
        return len(self.items)

    def print_deque(self):
        print(self.items)

player = Deque()
lista_comandos = []
musicas = []
todas_musicas = []
comando = [""]
while comando[0] != "fight":
    comando = input().split()
    if comando[0] == "play" or comando[0] == "add" or comando[0] == "del" or comando[0] == "next":
        lista_comandos.append(comando[0])
    if comando[0] == "play": # começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário).
        if not player.isEmpty():
            musica_atual = musicas[0]
            player.addFront(musica_atual)
            player.removeRear()
            for i in range (player.size()):
                musicas[i] = player.items[i]
            
    elif comando[0] == "stop": # interrompe a execução da música atual.
        pass
    elif comando[0] == "list": 
        if len(musicas) == 0: # Condição para lista vazia
            print("[vazia]")

        else:
            if len(musicas) == 1: # Quando tem apenas uma música
                print(musicas[0], end = '\n')
            else:   
                for i in range(len(musicas) - 1):
                    print(musicas[i], end = ',')
                print(musicas[-1], end = '\n') # Printa a última sem a vírgula             
    elif comando[0] == "current": # mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".
    # Pegará como referencia o play
        if player.isEmpty():
            print("Toque! Toque, Dijê")
        else:
            print(player.peek())
    elif comando[0] == "undo": # desfaz os efeitos de uma instrução add, del, next ou play. Isoladamente, desfaz o efeito da última instrução. Havendo o argumento opcional *, desfaz o efeito de todas as instruções dadas até aquele ponto.
        if len(lista_comandos) != 0:
            if lista_comandos[-1] == "add":
                player.removeFront()
                musicas.pop()
            elif lista_comandos[-1] == "del":
                for i in range(len(todas_musicas)-1): 
                    if todas_musicas[i] not in musicas:
                        player.addPosition(i, todas_musicas[i])
                        musicas.insert(i, todas_musicas[i])
                        break
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
            todas_musicas.append(comando[1])
        elif comando[0] == "del": # retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.
            if not player.isEmpty() and comando[1] in musicas:
                for i in range(len(musicas)-1):
                    if musicas[i] == comando[1]:
                        musicas.pop(i)
                        player.removePosition(i)
                        break   

        elif comando[0] == "next": # define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de id na lista é realocada para tanto
            if not player.isEmpty() and comando[1] in musicas:
                for i in range(len(musicas)):
                    if musicas[i] == comando[1]:
                        guarda = musicas[0] 
                        musicas[0] = musicas[i] 
                        musicas[i] = guarda
                player.items = musicas
    
print("Jedi Wagner, assuma o comando!")

# Analisar a possibilidade de retirar o Deque
