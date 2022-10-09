# take 2 float values and divide them

a = float(input('Enter the 1st no. '))
b = float(input('Enter the 2nd no. '))

# division
c = a/b

"""
other ways of precisely handling decimals include
print('%.6f' % c)
print(round(c, 6))
"""
print("{:.6f}".format(c))
