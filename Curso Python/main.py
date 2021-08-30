from calculadora import Calculador
from comodo import Comodo


calc = Calculador()

comodo = Comodo(
    input("Qual a largura do cômodo? "),
    input("Qual a profundidade do cômodo? ")
)

print(
    "A área da parede é: ", 
    calc.calcular_area_parede(comodo
    )
)

print(
    "A área do teto é: ",
    calc.calcular_area_teto(comodo
    )
)

print(
    "A litragem de tinta necessária é: ",
    calc.calcular_litragem_total()
)
