r = int(input())
count = 9
for k in range(r):
  for l in range(k+1):
    count += 1
    print(count, end=" ")
  print()