def contnum(cont):
    aux = 0
    total = 0
    for i in range(len(cont)):
        print(cont[i])
        if cont[i] == '1':
            j = i
            while True:
                aux += 1
                j += 1
                if cont[i] != '1':
                    break
            if cont[j] == '1':
                total += aux
                print(f'Total: {total}')
                aux = 0
            i += j
    return total

n = int(input())
for cont in range(n):
    s = input()
    print(contnum(s))