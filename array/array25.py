n = int(input())
a = [None] * n
index = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
if a[1] / a[0] == a[2] / a[1]:
  print(f"maxraj: {a[1] / a[0]}")
else:
  print(0)
