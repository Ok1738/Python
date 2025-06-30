import math
n = int(input("Daraja va faktorial uchun son kiriting: "))
x = float(input("Son kiriting: "))
print(math.cos(x))
sum = 0 
temp = 0
if n > 0:
  for i in range(n):
    temp = ((-1) ** i ) * (x ** (2*i))
    do = (2*i)
    factorial = 1
    for j in range(do):
      factorial *= (j + 1)
    sum += temp/factorial
print(sum)


  