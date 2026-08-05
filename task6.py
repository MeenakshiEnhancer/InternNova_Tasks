'''Create two user-defined functions:

Function to calculate the square of a number.
Function to calculate the average of three numbers.

Call both functions with user input.'''


def square(val):
    result=val*val
    return result

def average(num1,num2,num3):
    avg=(num1+num2+num3)/3
    return avg

val=int(input("Enter a number to find its square: "))
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

print(square(val))
print(round(average(num1,num2,num3),2))