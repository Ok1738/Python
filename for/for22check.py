n = int(input("Daraja va faktorial uchun son kiriting: "))
x = int(input("Son kiriting: "))
c = result = 1
if n > 0:
  for a in range(1,n+1):
    print(a, end=" daraja.\n")
    c *= a
    print(c, end=" faktorial.\n")
    result += (pow(x, a)/c)
  print(result)
  