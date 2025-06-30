n = int(input())
a = [None] * n
index = i = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
j = n - 1
while True: 
  print(a[i], a[j])
  if n % 2 == 0 : 
    if i == n/2-1:
      break
  if n % 2 == 1:
    if j == (n+1)/2:
      print(a[j-1])
      break
      

  i += 1 
  j -= 1