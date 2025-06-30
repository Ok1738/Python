n = int(input())
a = [None] * n
index = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
for x in range(0,n+1):
    if a[n-1] > a[x]:
      print("oxirgi elementidan kichkina bo'lgan birinchi element: ", a[x])
      break
    else:
      print(0)