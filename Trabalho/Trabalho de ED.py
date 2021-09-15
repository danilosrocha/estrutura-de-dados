# Funções
def play(msc, tcd_msc, lis_und):
    global iniciou
    iniciou += 1
    if len(msc) != 0:
        tcd_msc = True
        return tcd_msc
    else:
        lis_und.pop()
        tcd_msc = False
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
        if len(msc) == 1:
            print(msc[0])
        else:
            if tcd_msc == True:
                print(msc[0])
            else:
                print(msc[0])

def add(msc, lis_complt, cmd):
    if len(comando) < 2:
        return
    else:
        msc.append(cmd[1])
        lis_complt.append(cmd[1])
    return msc

def delet(msc, cmd, tcd_msc, lis_complt, ult_del, lis_und):
    global pos_del
    if len(cmd) < 2:
        return
    else:
        if tcd_msc == True:
            if cmd[1] == msc[0]:
                lis_und.pop()
            else:
                if cmd[1] in msc:
                    i = 0
                    while True:
                        if msc[i] == cmd[1]:
                            msc.pop(i)
                            pos_del = i
                            ult_del.insert(0, cmd[1])
                            break
                        i += 1
        else:
            if cmd[1] in msc:
                i = 0
                while True:
                    if msc[i] == cmd[1]:
                        msc.pop(i)
                        pos_del = i
                        ult_del.insert(0, cmd[1])
                        break
                    i += 1

def nexts(msc, lis_complt, cmd, tcd_msc):
    global posicao
    if len(comando) < 2:
        return 
    else:
        if len(msc) != 0 and cmd[1] in msc:
            if cmd[1] == msc [0]:
                return
            else:
                posicao = 0
                while True:
                    if msc[posicao] == cmd[1]:
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
                    posicao += 1

def ended(msc, lis_complt):
    if len(msc) != 0:
        musica_atual = msc[0]
        msc.append(musica_atual)
        msc.pop(0)
        for i in range (len(msc)):
            lis_complt[i] = msc[i]
        
    return msc, lis_complt

def undo(lis_und, msc, lis_complt, cmd, tcd_msc, ult_del, lis_ate_aqui):
    global posicao
    global iniciou

    if len(lis_und) != 0:

        if lis_und[-1] == "add":
            lis_und.pop()
            msc.pop()
            lis_complt.pop()
            return tcd_msc

        elif lis_und[-1] == "del":
            lis_und.pop()
            i = 0
            while True:
                if len(lis_complt) != 0:
                    if lis_complt[i] in ult_del:
                        msc.insert(pos_del, ult_del[i])
                        ult_del.pop(0)
                        break
                    else:
                        return
                i += 1
                
            return tcd_msc

        elif lis_und[-1] == "next":
            lis_und.pop()
            if tcd_msc == True:
                musica = msc[1]
                msc.remove(f"{msc[1]}")
                msc.insert(posicao, musica)
                lis_complt.remove(f"{lis_complt[1]}")
                lis_complt.insert(posicao, musica)
                return tcd_msc
            else:
                musica = msc[0]
                msc.remove(f"{msc[0]}")
                msc.insert(posicao, musica)
                lis_complt.remove(f"{lis_complt[0]}")
                lis_complt.insert(posicao, musica)
                

        elif lis_und[-1] == "play":
            iniciou -= 1
            lis_und.pop()
            if iniciou == 0:
                tcd_msc = False
                return tcd_msc
            else:
                tcd_msc = True
                return tcd_msc
    
    else:
        return tcd_msc
                
                
# Início do Programa
comando = [""]
musicas = []
lista_completa = []
lista_undo = []
ultimo_deletado = []
lista_ate_aqui = []
a = "a"
tocando_musica = False
tocou = 0
iniciou = 0
while comando[0] != "fight":
    comando = input().split()

    if len(comando) != 0:
        if comando[0] == "play" or comando[0] == "add" or comando[0] == "del" or comando[0] == "next":
            lista_undo.append(comando[0])
        if comando[0] == "play":
            tocando_musica = play(musicas, tocando_musica, lista_undo)
        elif comando[0] == "stop":
            tocando_musica = stop(musicas, tocando_musica)
        elif comando[0] == "list":
            listar(musicas)
        elif comando[0] == "current":
            current(musicas, tocando_musica, tocou)
        elif comando[0] == "undo":
            if len(comando) > 1:
                musicas = lista_ate_aqui
                if iniciou != 0:
                    tocando_musica = True
            else:
                tocando_musica = undo(lista_undo, musicas, lista_completa, comando, tocando_musica, ultimo_deletado, lista_ate_aqui)
              
        elif comando[0] == "add":
            add(musicas, lista_completa, comando)
        elif comando[0] == "del":
            delet(musicas, comando, tocando_musica, lista_completa, ultimo_deletado, lista_undo)
        elif comando[0] == "next":
            nexts(musicas, lista_completa, comando, tocando_musica)
        elif tocando_musica == True and comando[0] == "ended":
            ended(musicas, lista_completa)
            for i in range(len(musicas)):
                lista_ate_aqui.append(musicas[i])
            lista_undo = []

        if tocando_musica == True:
            tocou += 1
    else:
        comando = [""]

print("Jedi Wagner, assuma o comando!")
    
        
    