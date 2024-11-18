a = int(input("Son kiriting: "))  
b = int(input("Son kiriting: "))  
c = int(input("Son kiriting: "))   
difference = abs(a-b)
difference2 = abs(a-c)
if difference > difference2:
  print(c)
  print("Oradagi masofa: " + str(difference2))
elif difference2 > difference:
  print(b)
  print("Oradagi masofa: " + str(difference))
  
  