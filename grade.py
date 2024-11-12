print("--- Tell us your Grades ---")
grades = int(input("Grades: "))

if grades >= 100:
    print("Your Grade is A+")
elif grades < 100 and grades >= 90:
    print("Your grade is A")
elif grades < 90 and grades >= 80:
    print("Your Grade is B")
elif grades < 80 and grades >= 70:
    print("Your Grade is C")
elif grades < 70 and grades >= 60:
    print("Your Grade is D")
else:
    print("Your Grade is F")