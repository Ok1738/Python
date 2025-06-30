n = int(input())
a = [None] * n
index = S = S1 = 0
K, L = map(int, input("K va L ni kiriting: ").split())
while True: 
  a[index] = int(input())
  index += 1 
  if index == n:
    break
if 0 <= K <= L < n:
  for x in range(0, K):
    S += a[x]
  for j in range(L+1, n):
    S1 += a[j]
print(f"Kiritilgan {K} va {L} indekslari orasidan tashqaridagi elementlar yig'indisi: {S+S1}")