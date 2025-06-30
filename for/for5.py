a = float(input("Bir kg konfet uchun narx kiriting: "))   
n = 0  

for x in range(1, 11):  
    n = x * 0.1  
    print(f"{n:.1f} kg konfet uchun {a * n:.1f} so'm to'g'ri kelmoqda.") 