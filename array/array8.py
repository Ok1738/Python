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
  if x % 2 == 1:
    count += 1
toqlar_list = [None] * count
index = 0
for i in a:
  if i % 2 == 1:
    toqlar_list[index] = i
    index += 1

print("O'sish tartibida bo'lgan toq sonlar: ", toqlar_list)
print("Toq sonlar ", count, "ta.")
