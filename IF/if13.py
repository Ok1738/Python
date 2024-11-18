a = int(input("Son kiriting: "))  
b = int(input("Son kiriting: "))  
c = int(input("Son kiriting: "))   
if a >= b >= c or c >= b >= a:
  print(b)
elif c >= a >= b or b >= a >= c:
  print(a)
elif b >= c >= a or a >= c >= b:
  print(c)