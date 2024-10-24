a = int(input("Uch xonali son kiriting: "))
birlik = a % 10
onlik = a // 10 % 10
yuzlik = a // 100
print(yuzlik < onlik < birlik)