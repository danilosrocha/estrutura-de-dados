""" Programa que avalia a sua altura e peso

Altura média das mulheres é 1,62m
Altura média dos homens é 1,74m

IMC = peso/(altura^2)

Menor que 18,5 - Magreza
Entre 18,5 e 24,9 - Normal
Entre 25,0 e 29,9 - Sobrepeso
Entre 30,0 e 39,9 - Obesidade
Maior que 40,0 - Obesidade Grave

"""
#Função para comparar a altura média
def compara_altura_media(sexo, altura):
    """"Compara a Altura com a média do Brasil
    Entrada:
    sexo (string): identificação do sexo da pessoa
    altura (float): altura em metros da pessoa

    Saída:
    String: informa se a pessoa é mais alta ou baixa do que a media
    """
    if sexo == 'f':
        if altura < 1.62:
            saida = 'baixa'
        else:
            saida = 'alta'
        return saida
    else:
        if altura < 1.74:
            saida = 'baixo'
        else:
            saida = 'alto'
        return saida

#Função para calcular o IMC
def calcula_imc(peso, altura):
    """Calcula o IMC do usuario
    Entrada: 
        Peso (float): Peso em quilos da pessoa
        Altura (float): Altura em metros da pesso
    """
    return peso / (altura ** 2)
    
#Função para classificar o IMC
def classifica_imc(peso, altura):
    """String: informa a classificacao da pessoa

    """
    imc = calcula_imc(peso, altura)

    if imc < 18.5:
        saida = "MAGREZA"   
    elif 18.5 <= imc < 24.9:
        saida = "NORMAL"
    elif 24.9 <= imc < 29.9:
        saida = "SOBREPESO"
    elif 29.9 <= imc < 39.9:
        saida = "OBESIDADE"
    else:
        saida = "OBESIDADE GRAVE"

    return saida
#Entrada de Dados
nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo (F/M): ")
altura = float(input("Digite a sua altura (metros): "))
peso = float(input("Digite o seu peso (quilos): "))

print()
print(f"Olá {nome}, ")
print(f"Você é mais {compara_altura_media(sexo, altura)} do que a média brasileira!")
print (f'Seu imc é: {calcula_imc(peso, altura):.02f}')
print(f"E sua classificação de peso: {classifica_imc(peso, altura)}")