n = int(input())
a = [None] * n
a[0], d = map(int, input().split())

for i in range(1, n):
    a[i] = a[i - 1] + d

print(a)