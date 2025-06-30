import random
n = int(input())
a = [None] * n
index = 0
while True:
  b = random.randint(1,50)
  a[index] = b
  index += 1
  if index == n:
    break
print(a)
for x in range(n-1, -1, -1):
  print(a[x], end=" ")
  
  
""" instead of random"""
# n = int(input())
# a = [None] * n
# index = 0
# while True: 
#   a[index] = int(input())
#   index += 1 
#   if index == n:
#     break
# print(a)
