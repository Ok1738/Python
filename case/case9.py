a = int(input("Kunni aniqlash uchun son kiriting: ")) #kun
b = int(input("Oyni aniqlash uchun son kiriting: ")) #oy 
birliklar = a % 10 
onliklar = a //10
if b == 2:
  if (a >= 1 and a <= 27):
    a += 1
    print(a)
  else:
    print("Boshqattan urinib ko'ring!")
elif (b == 4 or b == 6 or b == 9 or b == 11):
  if a <= 1 and a >= 29:
    a += 1
    print(a)
elif (b <= 12 and b >= 1):
  if a <= 1 and a >= 30:
    a += 1
    print(a)
  else:
    print("Boshqattan urininb ko'ring!")
  
