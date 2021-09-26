n = int(input())
alunos = []
for i in range(n):
    ira = float(input())
    
    alunos.append(f"{ira:.2f}")
organizado = sorted(alunos, reverse = True)
while len(organizado) != 0:
    print(organizado.pop(0))
