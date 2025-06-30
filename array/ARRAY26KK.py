n = int(input())
a = [None] * n
index = cumulative_sum = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
# while True: 
#   if n % 2 == 0:
#       if a[index] % 2 == 0:
#         if a[index + 1] == 1:
#           index += 2
#         if index == n: 
#           print(0)
#           break 
#   if n % 2 == 1:
#     if a[index] % 2 == 1:
#         if a[n-1] == 0:
#           index += 2
#         if index-1 == n:
#           print(0)
#           break 
#         n-=1
while len(a) != cumulative_sum:
  if a[0] % 2 == 0:
    if a[0] % 2 == 0:
      cumulative_sum += 1 
    else:
      print(a[0])
    if a[1] % 2 == 1:
      cumulative_sum += 1
    else:
      print(a[1])
    a[0] = a[1]
    
  if a[0] % 2 == 1:
    if a[0] % 2 == 1:
      cumulative_sum += 1 
    else:
      print(a[0])
    if a[1] % 2 == 0:
      cumulative_sum += 1
    else:
      print(a[1])
print(cumulative_sum)