yil = int(input("Yilni aniqlash uchun son kiriting: "))
rang = (yil - 4) // 12 % 5 + 1
muchal = (yil - 4) % 12 + 1
if yil >= 4 and muchal > 0:
  match rang:
    case 1:
      print("Yashil ",end="")
    case 2:
      print("Qizil ", end="")
    case 3:
      print("Sariq ", end="")
    case 4:
      print("Oq ", end="")
    case 5:
      print("Qora ", end="")
  match muchal:
    case 1:
          print("sichqon yili.")
    case 2:
          print("sigir yili.")
    case 3:
          print("yo'lbars yili.")
    case 4:
        print("quyon yili.")
    case 5:
        print("ajdar yili.")
    case 6:
        print("ilon yili.")
    case 7:
        print("ot yili.")
    case 8:
        print("qo'y yili.")
    case 9:
      print("maymun yili.")
    case 10:
      print("tovuq yili.")
    case 11:
      print("it yili.")
    case 12:
      print("to'ng'iz yili.")
