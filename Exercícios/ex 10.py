n = int(input())
habilidades = (input().split())
soma_titulares = 0
soma_reservas = 0
habi_jog = []
habi_jog_res = []
if n >= 12:
    if len(habilidades) == n :
        quant_reservas = len(habilidades) - 11
        for i in range(len(habilidades)):
            habi_jog.append(int(habilidades[i]))
            habi_jog.sort(reverse = True)
        for k in range((n - 1), 10, -1):
            habi_jog_res.append(int(habi_jog[k]))
            habi_jog_res.sort(reverse = True)
        for j in range(11):
            soma_titulares += habi_jog[j]
        if len(habi_jog_res) > 11:
            for c in range(11):
                soma_reservas += habi_jog_res[c]
        else:
            for l in range(len(habi_jog_res)):
                soma_reservas += habi_jog_res[l]
             
        resultado = soma_titulares - soma_reservas
    print(resultado)


