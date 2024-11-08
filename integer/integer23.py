a = int(input("Sekund uchun Son kiriting: "))
print("Soatda hisoblanganda: " + str(int(a/3600)) + ", Va qolgan minut: " + str(int(a%3600/60)) + ", Va qolgan sekund: " + str(int(a%60)))