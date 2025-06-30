a, b = map(int, input().split())
count = 0
if a<b:
  for x in range(b - 1, a, -1):
    count += 1
    print(x)
  print(f"Chiqarilgan sonlar {count} ta.")
