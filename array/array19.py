n = int(input())
a = [None] * n
index = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
for x in range(n-1, 0, -1):
    if a[n-1] > a[x] > a[0]:
      print("oxirgi elementidan kichkina bo'lgan, birinchi elementidan katta bo'lgan oxirigi element: ", a[x])
      break
    else:
      print(0)
    