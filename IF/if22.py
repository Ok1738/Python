x = int(input("X uchun son kiriting: "))
y = int(input("Y uchun son kiriting: "))
if x != 0 and y != 0:
  if x > 0 and y > 0:
    print("Birinchi chorak.")
  if x < 0 and y > 0:
    print("Ikkinchi chorak.")
  if x < 0 and y < 0:
    print("Uchinchi chorak.")
  if x > 0 and y < 0:
    print("To'rtinchi chorak.")
else:
  print("Boshqattan urinib ko'ring!")
