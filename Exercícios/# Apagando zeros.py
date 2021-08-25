n = int(input()) # 
cont = 0
for i in range(n):
    zero = input()
    estado = 0
    aux = 0
    for j in zero:
        if j == '1' and estado == 0:
            estado = 1 # A procura do prox 0 
        elif j == '0' and estado == 1:
            aux += 1 # Achou o zero
            estado = 2 # A procura do prox 0
        elif j == '0' and estado == 2:
            aux += 1 # 
        elif j == '1' and estado == 2:
            cont += aux
            aux = 0
            estado = 1
    print(cont)
    cont = 0


    
 

        
            
        

