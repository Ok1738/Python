v = int(input("Qayiq tezligini kiriting(km/soat): "))
u = int(input("Oqim tezligini kiriting(km/soat): "))
t1 = int(input("Qayiq daryo oqimi bo'yicha harakatlanish vaqti uchun son kiriting(soat): "))
t2 = int(input("Qayiq daryo oqimga qarshi harakatlanish vaqti uchun son kiriting(soat): "))
print("Qayiq daryo oqimi bo'yicha yurganda masofa: " + str(t1*abs(v+u)) + "km ga teng bo'lsa, u oqimga qarshi yurganda: " + str(t2*abs(v-u)) + "km ga teng.")
