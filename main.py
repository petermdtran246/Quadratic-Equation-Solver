import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d= b*b-4*a*c

if d==0:
   print('Roots are real and equal')
elif d > 0:
   print('Roots are real and unequal')
   print(-b + math.sqrt(2 * a))
   print(-b - math.sqrt(2 * a))
else:
   print('Imaginary')
