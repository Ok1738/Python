n = int(input())
a = [None] * n
print(a)
index = 0
sonlar = 0
while True:
  a[index] = 2 ** sonlar
  index += 1
  sonlar += 1
  if index >= n:
    break

print(a)
print(len(a))