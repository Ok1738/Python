a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))
c = int(input("Son kiriting: "))
print("Bu teng yonli uchburchak bo'ladimi: ",(a == b and a != c and b != c) or (b == c and c != a and b != a) or (a == c and a != b and c != b))
