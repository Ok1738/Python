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
  index = 0
  for x in range(0, K):
    S += a[x]
    index += 1
  for j in range(L+1, n):
    S1 += a[j]
    index += 1
print(f"Kiritilgan {K} va {L} orasidan tashqaridagi elementlar yig'indisining o'rta arifmetigi: {(S+S1)/index}")