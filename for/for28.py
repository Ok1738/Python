n = int(input("Son kiriting n uchun: "))  
x = float(input("Son kiriting x uchun: "))
sum = 0 
if n > 0 and abs(x) < 1:  
  for i in range(1,n):
    surat = (-1 ** (i-1)) * (2*i - 3) * (x ** i)
    maxraj = 2 * i
    sum += surat/maxraj
  print(sum)
else:
  print("Boshqattan urinib ko'ring!")