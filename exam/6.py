m = int(input("9999 dan katta son kiriting: "))
yuzliklar = m // 100 % 10
print(yuzliklar)
onmingliklar = m // 10000 % 10
print(onmingliklar)

new_number = m - (yuzliklar * 100) - (onmingliklar*10000) + (yuzliklar*10000) + (onmingliklar*100)
print(new_number)