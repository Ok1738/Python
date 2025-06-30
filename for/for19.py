c = 1
n = int(input("Daraja uchun son kiriting: "))
if n > 0:
  for x in range(1, n+1):
    c *= x
print(c)