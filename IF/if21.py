x = int(input("X uchun son kiriting: "))
y = int(input("Y cuhun son kiriting: "))
if x == 0 and y == 0:
  print(0)
elif (x == 0 and y != 0) or (x != 0 and y == 0):
  x = 1
  y = 2
  print(x)
  print(y)
else: 
  print(3)