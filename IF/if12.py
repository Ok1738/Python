a = int(input("Son kiriting: "))  
b = int(input("Son kiriting: "))  
c = int(input("Son kiriting: "))   
if a >= b >= c or b >= a >= c:
  print(c)
elif c >= a >= b or a >= c >= b:
  print(b)
elif b >= c >= a or c >= b >= a:
  print(a)