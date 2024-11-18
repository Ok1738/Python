yil = int(input("Yilni aniqlash uchun son kiriting: "))
if yil > 0:
  if yil <= 100 and yil % 4 == 0:
      print("Bu yilda 366 kun bor.")
  elif yil >= 100 and yil % 400 != 0:
    print("Bu yilda 365 kun bor.")
  elif yil >= 100 and yil % 4 == 0:
    print("Bu yilda 366 kun bor.")
  