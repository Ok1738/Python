n = int(input())
a, b = map(int, input().split())
segment = 0
for x in range(a, b+1):
  segment += (b - a) / x
  print(segment)