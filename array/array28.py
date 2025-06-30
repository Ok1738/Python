n = int(input())
a = [None] * n
index = count = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
for x in a:
  if x % 2 == 0:
    count += 1
juftlar_list = [None] * count
index = 0
for i in range(n-1, -1, -1): 
  if a[i] % 2 == 0:
    juftlar_list[index] = a[i]
    index += 1
print(min(juftlar_list))