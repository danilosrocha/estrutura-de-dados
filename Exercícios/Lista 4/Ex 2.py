def peronio(str_1, str_2):
    global cont_1
    global cont_2
    nova_1 = list(str_1)
    nova_2 = list(str_2)
    if len(nova_1) == 0 and len(nova_2) == 0:
        return cont_1, cont_2
    else:
        if len(nova_1) != 0:
            cont_1 += 1
            nova_1.pop()
        if len(nova_2) != 0:
            cont_2 += 1
            nova_2.pop()
        return peronio(nova_1, nova_2)

cont_1 = 0
cont_2 = 0
a = input()
b = input()
print(peronio(a, b))

#peronio(a, b)


