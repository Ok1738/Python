n = int(input())
a = [None] * n
index = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
for x in range(0,n,2):
  print(x, ":JUFT-indeks:" , a[x])
for J in range(1, n, 2):
  print(J, ":TOQ-indeks: ", a[J])