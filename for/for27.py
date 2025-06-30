n = int(input("Son kiriting n uchun: "))  
x = float(input("Son kiriting x uchun: "))
sum = 0 
if n > 0 and abs(x) < 1:  
  for i in range(1,n):
    surat = (2*i-1) * (x ** (2*i+1))
    maxraj = (2 * i) * (2*i + 1)
    sum += surat/maxraj
  print(sum)
else:
  print("Boshqattan urinib ko'ring!")