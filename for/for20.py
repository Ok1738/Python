c = 1
j = 0
n = int(input("Son kiriting: "))
if n > 0:
  for x in range(1, n+1):
    c *= x
    j += c
print(j)

    