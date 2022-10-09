# solve quad eqn
import math

print('The form of a quadratic eqn is ax^2+bx+c')
a = int(input('Enter a '))
b = int(input('Enter b '))
c = int(input('Enter c '))

# determinant
d = math.sqrt((b**2)-4*a*c)

if d > 0:
    print('The root is real')
    x1 = (-b + d) / 2 * a
    x2 = (-b - d) / 2 * a
elif d == 0:
    print('The roots are equal')
    x1 = (d - b) / 2 * a
else:
    print('The roots are imaginary')

