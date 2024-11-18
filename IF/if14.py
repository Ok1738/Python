a = int(input("Son kiriting: "))  
b = int(input("Son kiriting: "))  
c = int(input("Son kiriting: "))   
if a >= b >= c :
  print(c)
  print(a)
elif b >= a >= c:
  print(c)
  print(b)
elif c >= a >= b:
  print(b)
  print(c)
elif a >= c >= b:
  print(b)
  print(a)
elif b >= c >= a:
  print(a)
  print(b)
elif c >= b >= a:
  print(a)
  print(c)