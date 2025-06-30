import math
a, b = map(int, input().split())
if a < b:
  n = 0
  for x in range(a,b+1):
    n += pow(x, 2)
  print(n)
else:
  print("Boshqattan urinib ko'ring.")