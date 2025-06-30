n = int(input())
a = [None] * n
index = count = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
for x in a:
  if x % 2 == 1:
    count += 1
toqlar_list = [None] * count
index = 0
for i in a:
  if i % 2 == 1:
    toqlar_list[index] = i
    index += 1
print(f"Maximum toq son: {max(toqlar_list)}")