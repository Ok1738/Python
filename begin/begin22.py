a = int(input("A uchun qiymat kiriting: "))
b = int(input("B uchun qiymat kiriting: "))
temp = a
a = b
b = temp
print("A ning qiymati: " + str(a))
print("B ning qiymati: " + str(b))

c = int(input("C uchun qiymat kiriting: "))
d = int(input("D uchun qiymat kiriting: "))
c = c + d
d = c - d
c = c - d
print("C ning qiymati: " + str(c))
print("D ning qiymati: " + str(d))