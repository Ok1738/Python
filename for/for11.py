n = int(input("N uchun son kiriting: "))
if n > 0:
  c = 0
  for x in range(n, 2*n+1):
    c += pow(x,2)
  print(c)
else:
  print("Boshqattan urinib ko'ring.")