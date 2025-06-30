a, b = map(int, input().split())
count = 0
if a<b:
  for x in range(a, (b+1)):
    count += 1
    print(x)
  print(f"Chiqarilgan sonlar {count} ta.")