a = int(input("Uch xonali son kiriting: "))
print("Kiritilgan sonni o'nliklar xonasidagi raqamni yuzliklar bilan almashtirganda: " + str(int(a/10%10)) + str(int(a/100)) + str(int(a%10)))