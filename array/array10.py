import random
n = int(input())
a = [None] * n
index = count = count1 = 0
while True:
  a[index] = random.randint(1, 1000)
  index += 1
  if index == n:
    break
print(a)
for x in a:
  if x % 2 == 0:
    count1 += 1
juftlar_list = [None] * count1
index = 0
for i in a: 
  if i % 2 == 0:
    juftlar_list[index] = i
    index += 1
for x in a:
  if x % 2 == 1:
    count += 1
toqlar_list = [None] * count
index = 0
for i in range(n-1, -1, -1):
  if a[i] % 2 == 1:
    toqlar_list[index] = a[i]
    index += 1
print("Indekslari o'sish tartibida joylashgan juft sonlar: ", juftlar_list)
print("Juft sonlar", count1, "ta.")
print("Indekslari kamayish tartibida joylashgan toq sonlar: ", toqlar_list)
print("Toq sonlar ", count, "ta.")