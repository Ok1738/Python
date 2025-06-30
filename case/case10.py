Y = (input("Robot qaysi yo'nalishda bo'lsin? (N - shimol, E - sharq, W - g'arb, S - janub) "
              "Kiriting: "))
K = int((input("Robot nima qilsin? (0 - harakatni davom ettir, 1 - chapga buril, 2 - o'ngga buril) "
              "Kiriting: ")))
if (Y == "N" or Y == "E" or Y == "W" or Y == "S") and (K == 0 or K == 1 or K == 2):
  match Y:
    case "N":
      print(" Shimol tomondan ", end="")
    case "E":
      print(" Sharq tomondan ", end="")
    case "W":
      print(" G'arb tomondan ", end="")
    case "S":
      print(" Janub tomondan", end="")
  match K:
    case 0:
      print(" harakatlan.", end="")
    case 1:
      print(" chapga.", end="")
    case 2:
      print(" o'ngga.", end="")
else:
  print("Boshqattan urinib ko'ring.")
