A,B = map(int, input("A va B uchun son kiriting: ").split())
if A < B: 
  for i in range(A, B+1):
    # print(i * f"{ i } ")
    print(i * str(i))