import random 
n = int(input("Juft son kiriting: "))
a = [None] * n
index = 0
for i in range(n):
  a[index] = random.randint(1, 100)
  index += 1
print(a)
for J in range(1, n, 2):
  print(J, ":TOQ-indeks: ", a[J])
for x in range(n-2,-2,-2):
  print(x, ":JUFT-indeks:" , a[x])
