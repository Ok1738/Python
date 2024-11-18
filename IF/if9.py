a = float(input("Son kiriting: ")) #kichik
b = float(input("Son kiriting: ")) #katta
if a > b:
  temp = a
  a = b
  b = temp
  print(a)
  print(b)
elif a < b:
  temp = b
  b = a
  a = temp
  print(a)
  print(b)
else:
  print("Ikkalasi teng.")