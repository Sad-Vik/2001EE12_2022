# Defining Function
def factorial(x):
    if x == 0:
        return 1
    elif x > 0:
        return x*factorial(x-1)  # Recursion
    else:
        return 'Enter a Valid Number!'


x = int(input("Enter the number whose factorial is to be found "))
Result = factorial(x)  # Calling the function
print(Result)
