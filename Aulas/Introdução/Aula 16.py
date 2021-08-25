"""Listas

Cadastro de notas APC

"""
def menu():
    while True:
        print('______________________')
        print()
        print('Opções:')
        print('1- Cadastra aluno')
        print('2- Entrada de notas')
        print('3- Ver extrato geral')
        op = int(input('Digite o numero da opção desejada: '))
        if 1 <= op <= 3:
            return op

def efetua_cadastro(cadastro):
    nome = input('Digite o seu nome: ')
    sobrenome = input('Digite o seu sobrenome: ')
    mat = input('Digite sua matrícula da UNB:')
    notas_le = [0.0] * 11
    cadastro.append([nome, sobrenome, mat, notas_le])


def entrada_notas(cadastro):
    if len(cadastro) == 0:
        print('Nenhum aluno cadastrado!')
    else:
        mat = input('Buscar pela matrícula: ')
        achou = False
        for i in range(len(cadastro)):
            if cadastro[i][2] == mat:
                achou = True
                print (f'Entre com as notas de {cadastro[i][0]} {cadastro[i][1]} ')
                for j in range(cadastro[i][3]):
                    cadastro[i][3][j] = float(input(f'Lista {j+1} ({cadastro[i][3][j]:.1f}: '))
                break
        if not achou:
            print(f'A matricula {mat} não foi encontrada.')

def calcula_media_lista(lista):
    return sum(lista) / len(lista)

def extrato(cadastro):
    for i in range(len(cadastro)):
        linha = '#' * (len(cadastro[i][0]) + len(cadastro[i][1]) + len(cadastro[i][2]) + 8) 
        print(linha)
        print(f'# {cadastro[i][0]} {cadastro[i][1]} ({cadastro[i][2]}) #')
        print(linha)
        for j in range(cadastro[i][3]):
            cadastro[i][3][j] = float(input(f'Lista {j+1} ({cadastro[i][3][j]:.1f}: '))
        media_li = calcula_media_lista(cadastro[i][3])
        print(f'LE = {media_li:.1f}')
# Inicio do programa
cadastro = []

continua = 's'
while continua != 'n':
    op = menu()

    if op == 1:
        efetua_cadastro(cadastro)
    elif op == 2:
        entrada_notas(cadastro)
    elif op == 3:
        extrato(cadastro)
    
    continua = input('Deseja continuar? (s/n) ')