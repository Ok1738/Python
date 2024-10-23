import math
x1 = int(input("Son kiriting: "))
y1 = int(input("Son kiriting: "))
x2 = int(input("Son kiriting: "))
y2 = int(input("Son kiriting: "))
length = abs(x2 - x1)
width = abs(y2 - y1)
A = length * width
P = 2*(length + width)
print("Yuzasi : " + str(A))
print("Perimetri: "  + str(P))

