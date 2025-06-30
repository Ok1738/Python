a = int(input("Uzunlik kiriting: ")) #uzunlik
b = int(input("Uzunlik qaysi birliklarda bo'lsin? "
              "(1 - desimetr , 2 - kilometr, 3 - metr, 4 - millimetr, 5 - santimetr)"
              "Kiriting: ")) 
match b:
  case 1:
    print("Desimetrdan metrga o'tganda: " + str(a/10))
  case 2:
    print( "Kilometrdan metrga o'tganda: "+str(a*1000))
  case 3:
    print("Metrda qolganda: " + str(a))
  case 4:
    print("Millimetrdan metrga o'tganda: " + str(a/1000))
  case 5:
    print("Santimetrdan metrga o'tganda: " + str(a/100))