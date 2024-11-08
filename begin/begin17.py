import math
a = int(input("A kesma uchun Son kiriting: "))
b = int(input("B kesma uchun Son kiriting: "))
c = int(input("C kesma uchun Son kiriting: "))
AC = c - a
BC = c - b
if a > b and b > c:
 print("AC kesma: " + str(abs(AC)) + " Va BC kesma: " + str(abs(BC)) + " Va o'sha kesmalar uzunligi yig'indisi: " + str(abs(AC + BC)))