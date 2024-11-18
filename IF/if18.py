a, b, c = map(int, input("Uchta butun son kiriting: ").split())
if a == b:
  print("Birinchi va ikkinchi kiritilgan sonlar teng, va "+ str(c) +" soni uchinchi bo'lib kiritildi.")
elif a == c:
  print("Birinchi va uchinchi kiritilgan sonlar teng, va "+ str(b) +" soni ikkinchi bo'lib kiritildi.")
elif b == c:
  print("Ikkinchi va uchinchi kiritilgan sonlar teng, va "+ str(a) +" soni birinchi bo'lib kiritildi.")
else:
  print("Bu dastur faqat 2 ta bir xil son kiritilganda ishlaydi.Boshqattan urinib ko'ring!")
  
  
