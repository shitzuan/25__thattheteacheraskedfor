# sum of numbers else than 100

a = int(input('Enter the last no. of the series  '))

t = 0 # for the total

for i in range(a+1):
    if i >= 100:
        break
    t += i
print(t)


"""
if the question was to take every no. from the user and find the sum then

c = 0
s = 0
while True :
    n = input('Enter a number ')
    if n == 'stop':
        break
    if n.isdigit() == True:
        c += n

print('The sum is {0} ')

"""