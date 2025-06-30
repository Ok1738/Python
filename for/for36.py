n = int(input("Son kiriting: "))
k = int(input("Son kiriting: "))
c = 0 
for x in range(1,n+1):
  c += pow(x, k)
print(c)