# multiplication table of a user given no.

a = int(input('Enter the no. whose multiplication table is needed'))
r = int(input('Enter the required range'))

for i in range(r+1):
    print(a, 'X', i, '=', a*i)
