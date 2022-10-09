# counter of +ve and -ve no.


c1 = 0
c2 = 0
while True:
    n = int(input('Enter a number '))
    if n == 0:
        break
    if n > 0:
        c1 += 1
    else:
        c2 += 1
print('The number of +ve no. is ', c1)
print('The number of -ve no. is ', c2)
