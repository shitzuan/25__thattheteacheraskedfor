# take value of binary digit by digit and display decimal

a = int(input('Enter leftmost digit '))
b = int(input('Enter the next digit '))
c = int(input('Enter the next digit '))
d = int(input('Enter the next digit '))


n = 0 # to store the decimal
if a == 1:
    n += 2**3
if b == 1:
    n += 2**2
if c == 1:
    n += 2**1
if d == 1:
    n += 2**0
# to print the decimal value of the entered binary
print(n)
