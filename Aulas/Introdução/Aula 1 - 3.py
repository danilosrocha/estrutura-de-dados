#Valores de entrada
nome = input("Digite seu nome: ")
n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))
f = int(input("Digite a sua frequência em %: "))

#Cálculo da nota final
n_f = ((n1 * 3 + n2 * 7) /10)

#Teste das condições para aprovação
if n_f >= 5 and f >= 75:
    print (f"Parabéns pela aprovação {nome}! Com a nota de {n_f}")
else:
    print (f"REPROVADO. Você tirou {n_f} e teve {f}% de frequência")