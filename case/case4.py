k = int(input("Son kiriting: "))
if k <= 12 and k >= 1:
  match k:
    case 1:
         print("Yanvarda 31 kun bor.")
    case 2:
         print("Fevralda 28/29 kun bor.")
    case 3:
         print("Martda 31 kun bor.")
    case 4:
        print("Aprelda 30 kun bor.")
    case 5:
        print("Mayda 31 kun bor.")
    case 6:
        print("Iyunda 30 kun bor.")
    case 7:
        print("Iyulda 31 kun bor.")
    case 8:
        print("Avgustda 31 kun bor.")
    case 9:
        print("Sentabrda 30 kun bor.")
    case 10:
        print("Oktabr 31 kun bor.")
    case 11:
        print("Noyabrda 30 kun bor.")
    case 12:
        print("Dekabrda 31 kun bor.")
else:
  print("xato.")