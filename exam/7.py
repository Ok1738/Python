import math
z = 3.5 * pow(10,-2)
x = 14.26
m = 1.3
p = 3.14
result = pow( (pow(10,5/4)*(abs(math.sin(pow(4, 5/4)) - z * x)) + pow(3*m + 2, 2)  + (math.cos(m)* (  (x- p/math.sqrt(m))/(3-2/math.sqrt(m))  )) ), 2/3 )
print(result)