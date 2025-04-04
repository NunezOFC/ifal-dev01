#Choose the Code
def main():
    print("--- Choice of Code ---")
    print("1 for Calculators")
    print("2 for Tellers")
    print("3 for Hello/Goodbye")
    code_choice = int(input("Choose your Code: "))
    if code_choice == 1:
        choice(code_choice)
    if code_choice == 2:
        choice(code_choice)
    if code_choice == 3:
        choice(code_choice)

def choice(code_choice):
    if code_choice == 1:
        print("1 for 5 Operaion Calculator")
        print("2 for Square/Cube Calculator")
        choice_code_2 = int(input("Choose your Code: "))
        if choice_code_2 == 1:
            calculator()
        else:
            square_number()
    elif code_choice == 2:
        print("1 for House Teller")
        print("2 for Grade Teller")
        print("3 for Pair Teller")
        choice_code_2 = int(input("Choose your Code: "))
        if choice_code_2 == 1:
            character()
        elif choice_code_2 == 2:
            grade()
        elif choice_code_2 == 3:
            pair()
    elif code_choice == 3:
        print("1 for Hello World")
        print("2 for Goobye World")
        print("3 for Input Name")
        print("4 for What Name")
        choice_code_2 = int(input("Choose your Code: "))
        if choice_code_2 == 1:
            hello()
        elif choice_code_2 == 2:
            goodbye()
        elif choice_code_2 == 3:
            input_name()
        elif choice_code_2 == 4:
            what_name()


#Calculator
def calculator():
   #Get the numbers
    x = float(input("Write the x Number:"))
    y = float(input("Write the y Number:"))

    #Choice of Operation
    print("Choose your Operation")
    print("1 for Division")
    print("2 for Abstraction")
    print("3 for Multiplication")
    print("4 for Sum")
    print("5 for Exponenciation")
    op = int(input("Write your Operation: "))
    calculation(op, x, y)

#Calculates the chosen numbers
def calculation(op, x, y):
    if op == 1:
        z = (x)/(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    elif op == 2:
        z = (x)-(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    elif op == 3:
        z = (x)*(y)
        z = f"{z:_.2f}"
    elif op == 4:
        z = (x)+(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    elif op == 5:
        z = (x)**(y)
        z = f"{z:_.2f}"
        z = z.replace(".", ",").replace("_",".")
    result(op, x, y, z)

#Result
def result(op, x, y, z):
    if op == 1:
        print(f"The Division between x and y is {z}")
    elif op == 2:
        print(f"The Abstraction between x and y is {z}")
    elif op == 3:
        print(f"The Multiplication between x and y is {z}")
    elif op == 4:
        print(f"The Sum between x and y is {z}")
    elif op == 5:
        print(f"The Exponenciation between x and y is {z}")

#square/cube number choice
def square_number():
    n = float(input("Write your number: "))
    exponencion_choice = input("Choose the Cube or Square of the Number: ")
    if exponencion_choice == "Cube":
        cube_calculator(n)
    else:
        square_calculator(n)

#square calculator
def square_calculator(n):
    print(f"the square of {n} is {n * n}")

#cube calculator
def cube_calculator(n):
    print(f"the square of {n} is {n * n * n}")

#Asks you about the Character   
def character():
    print("--- Harry Potter House Teller ---")
    character = input("Write a Harry Potter Character: ")
    house_teller(character)

#Verifies and tells you the Character
def house_teller(character):
    match character.title():
        case "Harry Potter"|"Harry"|"Potter"|"Rony"|"Weasley"|"Rony Weasley"|"Hermione Granger"|"Hermione":
            print("This character is from Gryffindor")
        case "Draco Malfoy"|"Draco"|"Malfoy":
            print("This character is from Slytherin")
        case "Luna Lovegood"|"Luna":
            print("This character is from Ravenclaw")
        case "Cedric Diggory"|"Cedric"|"Diggory":
            print("This character is from Hufflepuff")
        case _:
            print("No House Found")

#Asks you about your Grades
def grade():
    print("--- Tell us your Grades ---")
    grades = int(input("Grades: "))
    grade_teller(grades)

#Tells you Your Grade
def grade_teller(grades):
    if  97 <= grades <= 100:
        print("Your Grade is A+")
    elif 93<= grades <= 96:
        print("Your grade is A-")
    elif 90 <= grades <= 92:
        print("Your Grade is A")
    elif 87 <= grades <= 89:
        print("Your Grade is B+")
    elif 83 <= grades <= 86:
        print("Your Grade is B-")
    elif 80 <=grades <= 82:
        print("Your Grade is B")
    elif 77 <=grades <= 79:
        print("Your Grade is C+")
    elif 73 <= grades <= 76:
        print("Your Grade is C-")
    elif 70 <= grades <= 72:
        print("Your Grade is C")
    elif 67 <= grades <= 69:
        print("Your Grade is D+")
    elif 63 <= grades <= 66:
        print("Your Grade is D-")
    elif 60 <= grades <= 62:
        print("Your Grade is D")
    else:
        print("Your Grade is E/F")

#Asks you to write a Number
def pair():
    num = int(input("Write a Number: "))
    if pair_calculator(num):
        print("The number is Pair")
    else:
        print("The number is Unpaired")

#Verifys if the number is Pair
def pair_calculator(num):
    return num % 2 == 0

#Prints Hello, World
def hello():
    print("Hello, World")

#Prints Goodbye, World
def goodbye():
    print("Goodbye, World")

#Asks your name
def input_name():
    nome = input("What's your name? ")#Pergunta o Nome do Usuario
    nome = nome.title().split()
    nome(nome)

#prints your name
def nome(nome):
    nome = "💜".join(nome)
    print(nome)

#Asks your name
def what_name():
    nome = input("Qual seu nome? ")
    ola()
    ola(nome )

#Prints hello "Your name"
def ola(para="Mundo"):
    print("Olá", para.title())

main()
