#Problema: Calcular as raízes da função f(x) = ax^2 + bx + c

#Solução:
#Ler os vlaores de a, b e c
#Calcular as raízes quadráticas
    #Calcular o delta = b^2 -4ac
    #Se delta for negativa não há raiz
    #Dela = 0 (uma raiz)
    #Delta > 0 (duas raízes)
    #Calcular as raízes = -b +- raiz_quad(delta) / 2a
#Imprimir os resultados

# Entrada de dados
print("Cáculo de uma função quadrática ax^2 + bx + x.")
a = float(input("Entre com os valores A: "))
b = float(input("Entre com os valores B: "))
c = float(input("Entre com os valores C: "))

# Calcula delta 
def calc_delta(a, b, c):
    return b ** 2 - 4 * a * c

# Calcula as raizes da funçao quadratica
def calc_x1 (a, b, delta):
    return (- b + (delta ** 0.5)) / (2 * a)

def calc_x2 (a, b, delta):
    return (- b - (delta ** 0.5)) / (2 * a)

# Calcular e imprimir as raizes
def calc_raizes(a, b, c):
    delta = calc_delta(a, b, c)

    if delta < 0:
        print("Não há raízes reais")
    
    if delta == 0:
        x = calc_x1 (a, b, delta)
        print (f'x = {x:.2f}')

    if delta > 0:
        x1 = calc_x1 (a, b, delta)
        x2 = calc_x2 (a, b, delta)
        print (f'x1 = {x1:.2f}, x2 = {x2:.2f}')

# Imprime os dados
print()
calc_raizes(a, b, c)


