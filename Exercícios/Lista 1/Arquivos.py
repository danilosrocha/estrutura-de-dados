"""Dicionários e Tuplas

'' - strings (ordenada e imutável)
[] - Lista  (ordenada e mutável)
() - Tuplas (ordenada e imutável)

{} = Dicionario (desordenada e mutável)
"""
# Constante global
NUM_LISTAS = 11

# Funcoes
def menu():
    opções = {'1': 'Cadastra Aluno',
              '2': 'Entrada de notas',
              '3': 'Dados Aluno',
              '4': 'Ver extrato geral',  
              }
    while True:
        print('______________________')
        for opção, descricao in sorted(opções.items()):
            print(f'{opção}- {descricao}')
        opção = input('\nDigite o numero da opcao desejada: ')
        
        if opção in opções:
            return opção

def efetua_cadastro(cadastro):
    matricula = input('Digite sua matrícula da UNB: ')
    registra = True
    if matricula in cadastro:
        registro = cadastro[matricula]
        if input(f'{registro["nome"]} já está cadastrado.\n'
                 'Voce deseja sobrescrever o registro (s/n): ') == 'n':
            registra = False
    if registra:
        cadastro[matricula] = {'nome': input('Digite o seu nome completo: '),
                               'listas': [0.0] * NUM_LISTAS}

def entrada_notas(cadastro):
    if cadastro:
        matricula = input('Bsucar pela matricula: ')
        if matricula in cadastro:
            registro = cadastro[matricula]
            print(f'Entre com as notas de {registro["nome"]}: ')
            registro['lstas'] = [float(input(f'Lista {nota_le + 1}: '))
                                 for nota_le in range(NUM_LISTAS)]
        else:
            print(f'A matricula {matricula} nao foi encontrada.')
    else:
        print('Voce precisa cadastrar um aluno primeiro!')

# inicio do programa
nome = 'cadastro.bin'
cadastro = {}

#carrega o cadastro
if os.path.isfile(nome):
    with open(nome, 'rb') as arquivo:
        cadastro = pickle.load(arquivo)
        
continua = 's'
while continua != 'n':
    opção = menu()

    if opção == '1':
        efetua_cadastro(cadastro)
    if opção == '2':
        entrada_notas(cadastro)

    continua = input('Deseja continuar? (s/n): ')

#Salva o cadastro