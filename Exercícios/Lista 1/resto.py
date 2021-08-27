n, u = map(int, input().split()) 

parcial = n // u
resto = n - parcial * u

if resto == 0:
    print (resto)
else:
    print (1)
