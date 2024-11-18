a = int(input("Son kiriting: ")) #kichik
b = int(input("Son kiriting: ")) #katta
if a != b:
  if a > b:
    b = a
  elif a < b:
    a = b
elif a == b:
  a = 0
  b = 0
else:
  print("Ikkalasi teng.")
print(a)
print(b)