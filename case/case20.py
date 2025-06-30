oy = int(input("Oyni aniqlash uchun son kiriting: "))
kun = int(input("Kunni aniqlash uchun son kiriting: "))
if 1 <= kun <= 31 and 1 <= oy <= 12:
  match oy:
    case 1:
      if kun >= 20:
        print("Qovg'a.")
      elif kun <= 19:
        print("Echki.")
    case 2:
      if kun >= 19:
        print("Baliq.")
      elif kun <= 18:
        print("Qovg'a.")
    case 3:
      if kun >= 21:
        print("Qo'y.")
      elif kun <= 20:
        print("Baliq")
    case 4:
      if kun >= 20:
        print("Buzoq.")
      elif kun <= 19:
        print("Qo'y.")
    case 5:
      if kun >= 21:
        print("Egizaklar.")
      elif kun <= 20:
        print("Buzoq")
    case 6:
      if kun >= 22:
        print("Qisqichbaqa.")
      elif kun <= 20:
        print("Buzoq")
    case 7:
      if kun >= 23:
        print("Arslon.")
      elif kun <= 22:
        print("Qisqichbaqa.")
    case 8:
      if kun >= 23:
        print("Parizod.")
      elif kun <= 22:
        print("Arslon.")
    case 9:
      if kun >= 23:
        print("Tarozi.")
      elif kun <= 22:
        print("Parizod.")
    case 10:
      if kun >= 23:
        print("Chayon.")
      elif kun <= 22:
        print("Tarozi.")
    case 11:
      if kun >= 23:
        print("O'qotar.")
      elif kun <= 22:
        print("Chayon.")
    case 12:
      if kun >= 22:
        print("Echki.")
      elif kun <= 21:
        print("O'qotar.")
else:
  print("Boshqattan urinib ko'ring.")
  
      

