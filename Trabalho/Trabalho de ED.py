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

def current(msc, pos_msc_tcd):
    if len(msc) == 0:
            print("Toque! Toque, Dijê!")
    else:
        if len(msc) == 1:
            print(msc[0])
        else:
            print(msc[pos_msc_tcd])

def add(msc, lis_complt, cmd):
    global adicionou
    if len(comando) < 2:
        adicionou = False
        return 
    else:
        adicionou = True
        msc.append(cmd[1])
        lis_complt.append(cmd[1])
    return msc

def delet(msc, cmd, tcd_msc, pos_msc_tcd, ult_del, lis_und):
    global pos_del
    global deletou
    if len(cmd) < 2:
        deletou = False
        return pos_msc_tcd
    else:
        if len(msc) != 0:
            if tcd_msc == True:
                if cmd[1] == msc[pos_msc_tcd]:
                    deletou = False
                    return pos_msc_tcd
                else:
                    deletou = True
        
                    if cmd[1] in msc:
                        i = 0
                        while True:
                            if msc[i] == cmd[1]:
                                msc.pop(i)
                                pos_del = i
                                ult_del.insert(0, cmd[1])
                                pos_msc_tcd -= 1
                                return pos_msc_tcd
                                
                            i += 1
            else:                
                if cmd[1] in msc:
                    i = 0
                    pos_msc_tcd -= 1
                    while True:
                        if msc[i] == cmd[1]:
                            msc.pop(i)
                            pos_del = i
                            ult_del.insert(0, cmd[1])
                            deletou = True
                            return pos_msc_tcd
                        i += 1
                else:
                    deletou = False
                    return pos_msc_tcd
        else:
            deletou = False
            return pos_msc_tcd

def nexts(msc, lis_complt, cmd, tcd_msc, pos_msc_tcd, ult_nxt, lis_und):
    global nextoo
    if len(comando) < 2:
        nextoo = False
        return 
    else:
        if len(msc) != 0 and cmd[1] in msc:
            if cmd[1] == msc[pos_msc_tcd]:
                nextoo = False
                return
            else:
                nextoo = True
                ult_nxt.append(cmd[1])
                if pos_msc_tcd == 0 and tcd_msc == False:
                    msc.remove(f"{cmd[1]}")
                    lis_complt.remove(f"{cmd[1]}")
                    msc.insert(pos_msc_tcd, cmd[1])
                    lis_complt.insert(pos_msc_tcd, cmd[1])
                elif pos_msc_tcd != 0 and tcd_msc == False:
                    msc.remove(f"{cmd[1]}")
                    lis_complt.remove(f"{cmd[1]}")
                    if pos_msc_tcd == len(msc):
                        pos_msc_tcd = 0
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])
                else:
                    msc.remove(f"{cmd[1]}")
                    lis_complt.remove(f"{cmd[1]}")
                    if pos_msc_tcd == len(msc):
                        pos_msc_tcd = 0
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])
                    else:
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])                          
        else:
            nextoo = False
            return
def ended(msc, pos_msc_tcd): # A lista nao muda, só a posição que sim
    if len(msc) != 0:
        pos_msc_tcd += 1
        if pos_msc_tcd == len(msc):
            pos_msc_tcd = 0
        return pos_msc_tcd

def undo(lis_und, msc, lis_complt, cmd, tcd_msc, ult_del, pos_msc_tcd, ult_nxt):
    global iniciou
    
    if len(lis_und) != 0:
        if lis_und[-1] == "add":
            if adicionou == True:
                lis_und.pop()
                msc.pop()
                lis_complt.pop()
                return tcd_msc
            else:
                lis_und.pop()
                return tcd_msc

        elif lis_und[-1] == "del":
            if deletou == True:
                lis_und.pop()
                i = 0
                while True:
                    if len(lis_complt) != 0:
                        if lis_complt[i] in ult_del:  
                            msc.insert(pos_del, ult_del[0])
                            ult_del.pop(0)
                            break
                        else:
                            i += 1
                return tcd_msc
            else:
                lis_und.pop()
                return tcd_msc

        elif lis_und[-1] == "next": # Inserir a pos_msc_tcd
            if nextoo == True:
                lis_und.pop() 
                if pos_msc_tcd == 0 and tcd_msc == False:
                    msc.remove(f"{cmd[1]}")
                    lis_complt.remove(f"{cmd[1]}")
                    msc.insert(pos_msc_tcd, cmd[1])
                    lis_complt.insert(pos_msc_tcd, cmd[1])
                    return tcd_msc     
                elif pos_msc_tcd != 0 and tcd_msc == False:
                    msc.remove(f"{cmd[1]}")
                    lis_complt.remove(f"{cmd[1]}")
                    if pos_msc_tcd == len(msc):
                        pos_msc_tcd = 0
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])
                        return tcd_msc    
                    else:
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])     
                        return tcd_msc
                else:
                    msc.remove(f"{cmd[1]}")
                    lis_complt.remove(f"{cmd[1]}")
                    if pos_msc_tcd == len(msc):
                        pos_msc_tcd = 0
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])
                        return tcd_msc     
                    else:
                        msc.insert(pos_msc_tcd, cmd[1])
                        lis_complt.insert(pos_msc_tcd, cmd[1])     
                        return tcd_msc     
            else:
                lis_und.pop()
                return tcd_msc                 
               

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

def undo_2(lis_ate_aqui, msc, lis_und):
    if len(lis_und) != 0:
        msc = lis_ate_aqui
        return msc
    else:
        return msc
        
                
                
# Início do Programa
comando = [""]
musicas = []
lista_completa = []
lista_undo = []
ultimo_deletado = []
ultimo_next = []
lista_ate_aqui = []
deletou = False
adicionou = False
nextoo = False
tocando_musica = False
posicao_musica_tocando = 0
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
            current(musicas, posicao_musica_tocando)
        elif comando[0] == "undo":
            if len(comando) > 1:
                musicas = undo_2(lista_ate_aqui, musicas, lista_undo)
                lis_und = []
            else:
                tocando_musica = undo(lista_undo, musicas, lista_completa, comando, tocando_musica, ultimo_deletado, posicao_musica_tocando, ultimo_next)
              
        elif comando[0] == "add":
            add(musicas, lista_completa, comando)
        elif comando[0] == "del":
            posicao_musica_tocando = delet(musicas, comando, tocando_musica, posicao_musica_tocando, ultimo_deletado, lista_undo)
        elif comando[0] == "next":
            nexts(musicas, lista_completa, comando, tocando_musica, posicao_musica_tocando, ultimo_next, lista_undo)
        elif tocando_musica == True and comando[0] == "ended":
            posicao_musica_tocando = ended(musicas, posicao_musica_tocando)
            for i in range(len(musicas)):
                lista_ate_aqui.append(musicas[i])
            lista_undo = []

    else:
        comando = [""]

print("Jedi Wagner, assuma o comando!")
    
        
    