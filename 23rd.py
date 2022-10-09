# simulate a simple calc
# that means + - * /

print("Welcome to s simple python calc")
print('There are 4 possible operations')
print('Those are +, -, /, *')

# i'll input the operand to op n use a if chain to see what it is and accept no. and print outcomes
op = input('Enter your choice ')


if op == "+": # checking if the user want addition
    s = 0
    r = int(input('Enter the no. of numbers being given for summation')) # if the usr wants sum of more than 2 no.
    for i in range(r):
        a = int(input('Enter a no.'))
        s +=a
    print('The sum is', s)


elif op == "-": # checking if the user wants subtraction
    d = 0
    r = int(input('Enter the no. of numbers being given for finding the difference')) # if the user wants the difference of multiple no.
    for i in range(r):
        a = int(input('Enter a no.'))
        if i == 0:
            d = a
        else:
            d -= a
    print('The difference is', d)



elif op == "*": # checking if the user wants product
    p = 0
    r = int(input('Enter the no. of numbers being given for product')) # for product of multiple no.
    for i in range(r):
        a = int(input('Enter a no.'))
        p *= a
    print('The product is', p)



elif op == "/": # checking for division
    q = 0
    print('The format for division is a/b')
    a = int(input('Enter a'))
    b = int(input('Enter b'))
    q = a/b
    print('The quotient is', q)
else:
    print("Wrong choice")
