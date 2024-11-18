a, b, c, d = map(int, input("To'rtta butun son kiriting: ").split())
if a == b == c:
  print("Birinchi va ikkinchi va uchinchi kiritilgan sonlar teng, va "+ str(d) +" soni to'rtinchi bo'lib kiritildi.")
elif a == c == d:
  print("Birinchi va uchinchi va to'rtinchi kiritilgan sonlar teng, va "+ str(b) +" soni ikkinchi bo'lib kiritildi.")
elif b == c == d:
  print("Ikkinchi va uchinchi va to'rtinchi kiritilgan sonlar teng, va "+ str(a) +" soni birinchi bo'lib kiritildi.")
elif a == b == d:
  print("Birinchi va ikkinchi va to'rtinchi kiritilgan sonlar teng, va " + str(c) + "soni uchinchi bo'lib kiritildi.")
else:
  print("Bu dastur faqat 3 ta bir xil son kiritilganda ishlaydi.Boshqattan urinib ko'ring!")
  
  
