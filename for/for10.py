n = int(input("N uchun son kiriting: "))
if n > 0:
  c = 0
  for x in range(1, n+1):
    c += 1/x
  print(c)
else:
  print("Boshqattan urinib ko'ring.")