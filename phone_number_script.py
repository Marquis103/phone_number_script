##
# Write a script that prompts the user for their phone number, x. Then carry out the following steps:
 
# 1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)

# 2. Compute the sum of the digits of y, and store the result back in y.

# 3. Repeat step 2 until y has just one digit, then display it.
# author: marquis103
# assignment: MIDS Data Structures and Algorithms assignment

phoneNumber = int(input('Enter phone number '))

y = phoneNumber - sum([int(x) for x in str(phoneNumber)])

y = sum([int(x) for x in str(y)])

while len([int(x) for x in str(y)]) > 1:
	y = sum([int(x) for x in str(y)])

print(y)
