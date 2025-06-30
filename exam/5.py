m = int(input("4 xonali son kiriting: "))
birliklar = m % 10 
onliklar = m // 10 % 10
yuzliklar = m // 100 % 10
mingliklar = m // 1000
print(birliklar)
print(onliklar)
print(yuzliklar)
print(mingliklar)
print(birliklar+onliklar+yuzliklar+mingliklar)
print(str(onliklar) + str(yuzliklar) + str(mingliklar) + str(birliklar))
print(m - (mingliklar+yuzliklar+onliklar+birliklar))