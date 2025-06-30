import random
n = int(input())
a = [None] * n
index = count = 0
while True:
  a[index] = random.randint(1, 1000)
  index += 1
  if index == n:
    break
print(a)
for x in a:
  if x % 2 == 0:
    count += 1
juftlar_list = [None] * count
index = 0
for i in range(n-1, -1, -1): 
  if a[i] % 2 == 0:
    juftlar_list[index] = a[i]
    index += 1
print("Indekslari Kamayish tartibida joylashgan juft sonlar: ", juftlar_list)
print("Juft sonlar ", count, "ta.")