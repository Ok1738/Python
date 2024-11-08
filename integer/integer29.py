import math
a = int(input("A uchun son kiriting: "))
b = int(input("B uchun son kiriting: "))
c = int(input("C uchun son kiriitng: "))
joylashgan_qism = (a//c) * (b//c)
print("Joylashgan kvadratlar soni: " + str(int(joylashgan_qism)))
print("Joylashmagan qismi: "  + str((a*b) - (c*c*joylashgan_qism)))