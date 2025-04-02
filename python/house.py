#Asks you about the Character   
def main():
    print("--- Harry Potter House Teller  ---")
    character = str(input("Write a Harry Potter Character: "))
    house_teller(character)

#Verificates the Character house and informs it to the user
def house_teller(character):
    if  character == "Harry Potter" or "Harry" or "Hermione Granger" or "Hermione" or "Rony Weasley" or "Rony":
     print(f"{character} is from Gryffindor")
    elif character == "Draco Malfoy" or "Draco" or "Malfoy":
       print(f"{character} is from Slytherin")
    elif character == "Luna Lovegood" or "Luna":
       print(f"{character} is from Ravenclaw")
    elif character == "Cedric Diggory" or "Cedric" or "Diggory":
       print(f"{character} is from Hufflepuff")
    else:
       print("No House Found")

main()