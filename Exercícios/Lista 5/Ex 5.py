import operator

n = int(input())

Lista = []
for i in range(n):
    men, nome, sobre = input().split()
    completo = nome + " " + sobre
    if men == "SS":
        Lista.append("1 " + men + " " + completo)
    elif men == "MS":
        Lista.append("2 " + men + " " + completo)
    elif men == "MM":
        Lista.append("3 " + men + " " + completo)
    elif men == "MI":
        Lista.append("4 " + men + " " + completo)
    elif men == "II":
        Lista.append("5 " + men + " " + completo)
    else:
        Lista.append("6 " + men + " " + completo)
Lista.sort()

for i in range(len(Lista)):
    a = Lista[i] 
    print(a[2:])



    
    