"""
import time
import matplotlib.pyplot as plt

#?O(n)?
def complexidade1(n):
    inicio = time.time()
    while n > 0:
        n -= 1
    fim = time.time()
    return fim - inicio

#?O(log*n)?
def complexidade2(n):
inicio = time.time()
while n > 0:
n = n/2
fim = time.time()
return fim - inicio


#?O(1)?
def complexidade3(n):
inicio = time.time()
n**2 # 1u.t.
fim = time.time()
return fim - inicio

tc1 = []
tc2 = []
tc3 = []

for i in range(1, 1000000, 100000):
tc1.append(complexidade1(i))

for i in range(1, 1000000, 100000):
tc2.append(complexidade2(i))

for i in range(1, 1000000, 100000):
tc3.append(complexidade3(i))

#print(tc1)
#print(tc2)
#print(tc3)

n = range(1, 1000000, 100000)

plt.plot(n,tc1)
plt.plot(n,tc2)
plt.plot(n,tc3)
plt.show()
"""