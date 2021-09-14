# Funções
def play(msc, tcd_msc):
    if len(msc) != 0:
        tcd_msc = True
        return tcd_msc
    else:
        return tcd_msc

def stop(msc, tcd_msc):
    if len(msc) != 0:
        tcd_msc = False
        return tcd_msc
    else:
        return tcd_msc

def listar(msc):
    if len(msc) == 0: # Condição para lista vazia
            print("[vazia]")
    else:
        if len(msc) == 1: # Quando tem apenas uma música
            print(msc[0], end = '\n')
        else:   
            for i in range(len(msc) - 1):
                print(msc[i], end = ',')
            print(msc[-1], end = '\n') # Printa a última sem a vírgula 

def current(msc, tcd_msc, tc):
    if len(msc) == 0:
            print("Toque! Toque, Dijê!")
    else:
        """if tcd_msc == True:
            if tc < 2 and len(msc) > 1:
                print(msc[1])
            else:
                print(msc[0])
        else:"""
        print(msc[0])

def add(msc, lis_complt, cmd):
    if len(comando) < 2:
        return
    else:
        msc.append(cmd[1])
        lis_complt.append(cmd[1])
    return msc

def delet(msc, cmd):
    if len(cmd) < 2:
        return
    else:
        if cmd[1] in msc:
            i = 0
            while True:
                if msc[i] == cmd[1]:
                    msc.pop(i)
                    break
                i += 1
        else:
            return

def nexts(msc, lis_complt, cmd, tcd_msc):
    if len(comando) < 2:
        return 
    else:
        if len(msc) != 0 and cmd[1] in msc:
            if cmd[1] == msc [0]:
                return
            else:
                i = 0
                while True:
                    if msc[i] == cmd[1]:
                        if tcd_msc == True:
                            msc.remove(f"{cmd[1]}")
                            msc.insert(1, cmd[1])
                            lis_complt.remove(f"{cmd[1]}")
                            lis_complt.insert(1, cmd[1])
                            break
                        else:
                            msc.remove(f"{cmd[1]}")
                            msc.insert(0, cmd[1])
                            lis_complt.remove(f"{cmd[1]}")
                            lis_complt.insert(0, cmd[1])
                            break
                    i += 1

def ended(msc, lis_complt):
    if len(msc) != 0:
        musica_atual = msc[0]
        msc.append(musica_atual)
        msc.pop(0)
        for i in range (len(msc)):
            lis_complt[i] = msc[i]
        
    return msc, lis_complt

def undo(lis_und, msc, lis_complt, cmd):
    if len(msc) != 0:
        if len(cmd) == 2: # Condicao para entrar no undo *
            if cmd[1] == "*":
                for i in range(len(lis_und)):
                    msc.pop()
                    lis_complt.pop()
            else:
                return
        else:
            if len(lis_und) != 0:
                if lis_und[-1] == "add":
                    msc.pop()
                    lis_complt.pop()
                elif lis_und[-1] == "del":
                    i = 0
                    while True:
                        if lis_complt[i] not in msc:
                            msc.insert(i, lis_complt[i])
                            break
                        i += 1
                elif lis_und[-1] == "next":
                    pass
                elif lis_und[-1] == "play":
                    pass
    else:
        return
    
    


# Início do Programa
comando = [""]
musicas = []
lista_completa = []
lista_undo = []
tocando_musica = False
tocou = 0
while comando[0] != "fight":
    comando = input().split()
    if comando[0] == "play" or comando[0] == "add" or comando[0] == "del" or comando[0] == "next":
        lista_undo.append(comando[0])
    if comando[0] == "play":
        tocando_musica = play(musicas, tocando_musica)
    elif comando[0] == "stop":
        tocando_musica = stop(musicas, tocando_musica)
    elif comando[0] == "list":
        listar(musicas)
    elif comando[0] == "current":
        current(musicas, tocando_musica, tocou)
    elif comando[0] == "undo":
        undo(lista_undo, musicas, lista_completa, comando)
    elif comando[0] == "add":
        add(musicas, lista_completa, comando)
    elif comando[0] == "del":
        delet(musicas, comando)
    elif comando[0] == "next":
        nexts(musicas, lista_completa, comando, tocando_musica)
    elif tocando_musica == True and comando[0] == "ended":
        ended(musicas, lista_completa)
        lista_undo = []
    if tocando_musica == True:
        tocou += 1

print("Jedi Wagner, assuma o comando!")
    
        
    