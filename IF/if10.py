a = int(input("Son kiriting: ")) #kichik
b = int(input("Son kiriting: ")) #katta
if a != b:
  a = a + b
  b = a + b
  print(a)
  print(b)
elif a == b:
  a = 0
  b = 0
  print(a)
  print(b)
else:
  print("Ikkalasi teng.")