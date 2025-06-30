import math
r = int(input("Silindr radiusini kiriting: "))
h = int(input("Silindr balandligini kiriting: "))
S_asos = math.pi*r*r
S_yon = 2*math.pi*r*h
S_tula = S_yon + 2*S_asos
V = S_asos*h
print(S_asos)
print(S_yon)
print(S_tula)
print(V)