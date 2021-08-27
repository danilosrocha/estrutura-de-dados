# Input str
data_inicial = input()
data_final = input()

# Transformando a str em int (Inicial)
data_separada = data_inicial.split()

dia_inicial = int(data_separada[0])
hr_min_seg = data_separada[1]

horario_inicial = hr_min_seg.split(":")
hora_inicial = int(horario_inicial[0])
min_inicial = int(horario_inicial[1])
seg_inicial = int(horario_inicial[2])

# Transformando a str em int (Final)
data_separada_final = data_final.split()

dia_final = int(data_separada_final[0])
hr_min_seg_2 = data_separada_final[1]

horario_final = hr_min_seg_2.split(":")
hora_final = int(horario_final[0])
min_final = int(horario_final[1])
seg_final = int(horario_final[2])

# Dias em segundos
dia_seg_inicial = dia_inicial * 86400
dia_seg_final = dia_final * 86400

# Horas em segundos
hora_seg_inicial = hora_inicial * 3600
hora_seg_final = hora_final * 3600

# Minutos em segundos
min_seg_inicial = min_inicial * 60
min_seg_final = min_final * 60

# Segundos totais
seg_total_inicial = dia_seg_inicial + hora_seg_inicial + min_seg_inicial + seg_inicial
seg_total_final = dia_seg_final + hora_seg_final + min_seg_final + seg_final

# Duracao total
duracao = seg_total_final - seg_total_inicial

# Duracao em dias
duracao_dia = duracao // 86400
duracao_dia_seg = duracao_dia * 86400

# Duracao em horas
duracao_hora = (duracao - duracao_dia_seg) // 3600
duracao_hora_seg = duracao_hora * 3600

# Duracao em minutos
duracao_min = (duracao - duracao_dia_seg - duracao_hora_seg) // 60
duracao_min_seg = duracao_min * 60

# Duracao em segundos
duracao_seg = duracao - duracao_dia_seg - duracao_hora_seg - duracao_min_seg

# Condições de existencia p/ datas (Olhar os horarios negativos)
if (seg_final > 59 or seg_final < 0) or (seg_inicial > 59 or seg_inicial < 0):
    print("Data inválida!")
elif (min_final > 59 or min_final < 0) or (min_inicial > 59 or min_inicial < 0):
    print("Data inválida!")
elif (hora_final > 23 or hora_final < 0) or (hora_inicial > 23 or hora_inicial < 0):
    print("Data inválida!")
elif (dia_final > 31 or dia_final < 0) or (dia_inicial > 31 or dia_inicial < 0):
    print("Data inválida!")
elif duracao < 0:
    print("Data inválida!")
else:
    print(f'{duracao_dia} dia(s)')
    print(f'{duracao_hora} hora(s)')
    print(f'{duracao_min} minuto(s)')
    print(f'{duracao_seg} segundo(s)')


    


