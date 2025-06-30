n = int(input("N sonini kiriting: "))  
sum = 0  
for i in range(1, n + 1):  
    sum += pow(i, n - (i - 1))
print("Yig'indi: ", sum)