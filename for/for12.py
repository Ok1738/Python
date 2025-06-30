n = int(input())
c = 1
if n > 0:
 for x in range(1, n+1):
   x = (x / 10) + 1
   c *= x
print(c)