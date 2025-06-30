import math
n = int(input("Daraja va faktorial uchun son kiriting (n): "))
x = float(input("Son kiriting (x): "))
print(math.sin(x))
sum = 0 
temp = 0
if n > 0:
  for i in range(n):
    temp = ((-1) ** i ) * (x ** (2*i+1))
    do = (2*i + 1)
    factorial = 1
    for j in range(do):
      factorial *= (j + 1)
    sum += temp/factorial
print(sum)


  