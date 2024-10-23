n = int(input("Hafta kunlari uchun son kiriting: (1 - dushanba yoki 7 - yakshanba): "))
print("1 yanvar " + str(n) + "ga to'g'ri kelmoqda.")
k = int(input("Son kiriting: "))
print((k%7 + n - 1)%7)


