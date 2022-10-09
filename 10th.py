# take 2 no. and divide the 1st by the 2nd and display 2 decimal places

a = int(input('Enter the 1st no. '))
b = int(input('Enter the 2nd no. '))


c = a/b

"""
other ways of precisely handling decimals include
print('%.2f' % c)
print(round(c, 2))
"""
print("{:.2f}".format(c))

