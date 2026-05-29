# simple additon of two number in python

#define a fucntion to add two number
def sum(a , b):
    sum = a + b 
    return sum

# take a two interger number of users.
firstNumber= int(input("Enter a number a : "))
secondNumber= int(input("please enter a number b: "))
result =sum(firstNumber , secondNumber)  # function call
print(f"The sum of two number is {result}") #print a result sums of two number