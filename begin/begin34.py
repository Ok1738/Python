x = int(input("Shokoladni kg da kiriting: "))
a = int(input("Endi uni narxini kiriting: "))
y = int(input("Konfetni kg da kiriting: "))
b = int(input("Endi uni ham narxini kiriting: "))
bir_kg_shokolad = int(a/x)
bir_kg_konfet = int(b/y)
print("1 kg shokolad 1 kg konfetdan " + str(abs(bir_kg_shokolad - bir_kg_konfet)) + " so'm qimmat turadi.")