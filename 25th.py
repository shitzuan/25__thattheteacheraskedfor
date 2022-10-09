# palindrome

a = input('Enter a no.')
l = len(a)
n = int(a)
l -= 1


x1 = n % 10 # to take the last no

x2 = n // 10**l # to take the 1st no

# to check the 1st and last no.
if x1 == x2:
    print('The given no. is a palindrome')
else:
    print('The given no. is not a palindrome')
