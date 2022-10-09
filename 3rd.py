# binary to decimal

a = int(input("Enter the binary to convert to decimal  "))

i = 0 # for incrementing and conversion
d = 0 # for the digit extractor
n = 0 # the no. will be stored here
# for loop to run a digit extractor
while a > 0:
    d = a % 10
    a //= 10
    if d == 1:
        n += 2**i
    i += 1

# printing the decimal outside the loop
print(n)
