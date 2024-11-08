a1 = int(input("A koiffisenti uchun son kiriting: "))
b1 = int(input("B koiffisenti uchun son kiriting: "))
c1 = int(input("C koiffisenti uchun son kiriting: "))
a2 = int(input("D koiffisenti uchun son kiriting: "))
b2 = int(input("E koiffisenti uchun son kiriting: "))
c2 = int(input("F koiffisenti uchun son kiriting: "))
D = a1*b2 - a2*b1
x = (c1*b2 - c2*b1)/D
y = (a1*c2- a2*c1)/D
print("Chiziqli tenglamada x " + str(x) + " ga teng, va y " + str(y) + " ga teng.")


