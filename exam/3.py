import math
a = int(input("A kesma uchun Son kiriting: "))
b = int(input("B kesma uchun Son kiriting: "))
if a > b:
  print("Joylashgan qismi: " + str(a//b) + " va joylashmagan qismi: " + str(b-a%b))
else: 
  print("Shartga mos kelmaydi.")
