a = int(input("Son kiriting: "))
if a >= 1 and a <= 999:
  if a % 2 == 0 and a >= 1 and a <= 10:
    print("Kiritilgan son 1 xonali juft son.")
  elif a % 2 == 1 and a >= 1 and a <= 10:
    print("Kiritilgan son 1 xonali toq son.")
  elif a % 2 == 0 and a <= 99 and a >= 10:
    print("Kiritilgan son 2 xonali juft son.")
  elif a % 2 == 1 and a <= 99 and a >= 10:
    print("Kiritilgan son 2 xonali toq son.")
  elif a % 2 == 0 and a >= 100 and a <= 999:
    print("Kiritilgan son 3 xonali juft son.")
  elif a % 2 == 1 and a >= 100 and a <= 999:
    print("Kiritilgan son 3 xonali toq son.")
else:
  print("Boshqattan urinib ko'ring!")
