a = int(input("Son kiriting: "))  
b = int(input("Son kiriting: "))  
c = int(input("Son kiriting: "))   
sum = 0  
sum_neg = 0
if a > 0:  
    sum += 1  
if b > 0:  
    sum += 1  
if c > 0:  
    sum += 1  
if a < 0:
  sum_neg += 1
if b < 0:
  sum_neg += 1
if c < 0:
  sum_neg += 1

print("Musbat sonlar " + str(sum) + " ta, va manfiy sonlar " + str(sum_neg) + " ta.") 