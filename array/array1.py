n = int(input())
a = [None] * n
print(a)
index = 0
sonlar = 1
while True:
  if sonlar%2 == 1:
    a[index] = sonlar
    index += 1
  sonlar += 1
  if index >= n:
    break
  
print(a)
print(len(a))