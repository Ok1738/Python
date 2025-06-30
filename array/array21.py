n = int(input())
a = [None] * n
index = S = 0
K, L = map(int, input("K va L ni kiriting: ").split())
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
if 0 <= K <= L < n:
  index = 0 
  for x in range(K, L+1,):
    S += a[x]
    index += 1
print(S/index)