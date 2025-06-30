a, b = map(int, input("A va B uchun sonlar kiriting: ").split())
if a < b:
  d = 0 
  for i in range(a, b+1):
    for j in range(d+1):
      print(i, end=" ")
    print("\n")
    d += 1