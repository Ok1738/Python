n, K = map(int,input().split())
a = [None] * n
index = 0
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
if 1 <= K < n:
  for x in range(K, n, K):
    print(x, "-indeks: ", a[x])
    