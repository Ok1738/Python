a = int(input("Son kiriting: "))
if a > 0 and a % 2 == 1:
  print("Kiritilgan son musbat toq son.")
elif a < 0 and a % 2 == 1:
  print("Kiritilgan son manfiy toq son.")
elif a > 0 and a % 2 == 0:
  print("Kirilgan son musbat juft son.")
elif a < 0 and a % 2 == 0:
  print("Kirilgan son manfiy juft son.")
elif a == 0:
  print("Kiritilgan son nolga teng.")
