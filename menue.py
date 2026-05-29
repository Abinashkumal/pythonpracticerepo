
# define a functin for perform a task
def sum():
    firstNumber = int(input("Please enter a firstNumber: "))
    secondNumber = int(input("please Enter a secondNumber: "))
    sum = firstNumber + secondNumber
    result = sum
    print(f"The sum of two number is {result}")
    return result

def sub():
    firstNumber =int(input("please enter a firstNumber: "))
    secondNumber = int(input("please enter a secondNumber: "))
    sub = firstNumber - secondNumber
    result = sub
    print(f"The sub of two number is : {sub}")
    return result


def mul():
    firstNumber =int(input("please enter a firstNumber: "))
    secondNumber = int(input("please enter a secondNumber: "))
    mul = firstNumber * secondNumber
    result = mul
    print(f"The sub of two number is : {mul}")
    return result



def div():
    firstNumber =int(input("please enter a firstNumber: "))
    secondNumber = int(input("please enter a secondNumber: "))
    div = firstNumber/ secondNumber
    result = div
    print(f"The sub of two number is : {div}")
    return result



# Using a loop to display menue and perform task 

while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.exist!")

    choice = input("Please choose a valid number: ")

# using if elif  concep f
    if choice == "1":
        sum()
    elif choice == "2":
        sub()
    elif choice== "3":
        mul()
    elif choice =="4":
        div()
    elif choice =="5":
        print("Exist")
        break

 

#  Ask a user to perform a task again or not

    again =input(("Do you want to perform task again(y/n):")).lower()  # using a lower function also if user enter a capital letter to give input in lowercase
    if again =='y':
        print("\n\n\n--welcome----")
    else:
        print("Thankyou!")
        break
    

    