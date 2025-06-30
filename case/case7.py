a = int(input("Og'irlik uchun son kiriting: ")) #ogirlik
b = int(input("Og'irlik qaysi birliklarda bo'lsin? "
              "(1 - kilogram , 2 - milligram, 3 - gram, 4 - tonna, 5 - sentner)"
              "Kiriting: ")) 
match b:
  case 1:
    print("Kilogramda qolganda: " + str(a))
  case 2:
    print("Milligramdan kilogramga o'tganda: "+str(a/1000000))
  case 3:
    print("Gramdan Kilogramda o'tganda: " + str(a/1000))
  case 4:
    print("Tonnadan Kilogramga o'tganda: " + str(a*1000))
  case 5:
    print("Sentnerdan Kilogramga o'tganda: " + str(a*100))