n = int(input())
a = [None] * n
index = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
i = 0
while True: 
  if n % 2 == 0 : 
    if i + 1 == (n/2)-1:
      break
    print(a[i], a[i+1], a[n-1], a[n-2])
  if n % 2 == 1:
    if i+1 == (n//2):
      print(a[i+1])
      break
    print(a[i], a[i+1], a[n-1], a[n-2])
  i += 1
  n -= 1
