n = int(input())
A, B = map(int, input().split())
index = 2
a = [None] * n
a[0] = A
a[1] = B
if n > 2:
  while True:
    a[index] = A + B
    B = A
    A = a[index]
    index += 1
    if index == n:
      break
    
print(a)