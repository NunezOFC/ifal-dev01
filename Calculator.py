#Calculator
def calculator():
   #Get the numbers
    x = float(input("Write the First Number:"))
    y = float(input("Write the Second Number:"))

    #Choice of Operation
    print("Choose your Operation")
    print("1 for Division")
    print("2 for Abstraction")
    print("3 for Multiplication")
    print("4 for Sum")
    print("5 for Exponenciation")
    operation = int(input("Write your Operation:"))

    #Calculates the chosen numbers
    if operation == 1:
        z = (x)/(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    elif operation == 2:
        z = (x)-(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    elif operation == 3:
        z = (x)*(y)
        z = f"{z:_.2f}"
    elif operation == 4:
        z = (x)+(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    elif operation == 5:
        z = (x)**(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")

    #Result
    if operation == 1:
        print(f"The Division between {x} and {y} is {z}")
    elif operation == 2:
        print(f"The Abstraction between {x} and {y} is {z}")
    elif operation == 3:
        print(f"The Multiplication between {x} and {y} is {z}")
    elif operation == 4:
        print(f"The Sum between {x} and {y} is {z}")
    elif operation == 5:
        print(f"The Exponenciation between {x} and {y} is {z}")

calculator()
