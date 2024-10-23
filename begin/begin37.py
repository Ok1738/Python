import math
v1 = int(input("Birinchi avtomobil tezligi uchun son kiriting(km/soat): "))
v2 = int(input("Ikkinchi avtomobil tezligi uchun son kiriting(km/soat): "))
t = int(input("Vaqt uchun son kiriting(soat): "))
print("Berilganlarga asoslangan holda topilgan masofa: " + str(t*(v1+v2)))