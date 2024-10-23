#Get the Numbers
def calculation():
    x = input("Write the First Number:")
    y = input("Write the Second Number:")

    #Choice of Operation
    print("Choose your Operation")
    print("1 for Division")
    print("2 for Abstraction")
    print("3 for Multiplication")
    print("4 for Sum")
    operation = int(input("Write your Operation:"))

    #Calculates the chosen numbers
    if operation == 1:
        z = int(x)/int(y)
    elif operation == 2:
        z = int(x)-int(y)
    elif operation == 3:
        z = int(x)*int(y)
    elif operation == 4:
        z = int(x)+int(y)

    #Result
    if operation == 1:
        print(f"The Division between {x} and {y} is {z}")
    elif operation == 2:
        print(f"The Abstraction between {x} and {y} is {z}")
    elif operation == 3:
        print(f"The Multiplication between {x} and {y} is {z}")
    elif operation == 4:
        print(f"The Sum between {x} and {y} is {z}")
