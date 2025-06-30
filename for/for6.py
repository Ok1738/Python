a = float(input("Bir kg konfet uchun narx kiriting: "))   
n = 0  
for x in range(6, 11, 1): 
    n = x * 0.2
    print(f"{n:.1f} kg konfet uchun {a * n:.1f} so'm to'g'ri kelmoqda.") 