n = int(input())
c = 0
if n > 0:
  for x in range(1,2*n,2):
    c += x ** 2
  print(c)