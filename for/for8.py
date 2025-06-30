a, b = map(int, input("A va B uchun sonlar kiriting: ").split())
if a < b:
  n = 1
  for x in range(a,b+1):
    n = x * n
  print(n)
else:
  print("Birinchi kiritilgan son keyingisidan kichikroq bo'lishi kerak.")