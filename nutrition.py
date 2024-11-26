
foods = [   
    {"name":"Maçã", "calorias":"52kcal", "gorduras":"0,2g", "carboidratos":"14g", "proteinas":"0,3g"},
    {"name":"Banana", "calorias":"89kcal", "gorduras":"0,3", "carboidratos":"23g", "proteinas":"1,1g"},
    {"name":"Uva", "calorias":"67kcal", "gorduras":"0,4g", "carboidratos":"17g", "proteinas":"0,6g"},
    {"name":"Picanha", "calorias":"325kcal", "gorduras":"26,7g", "carboidratos":"0g", "proteinas":"19,72g"}
  ]

for  food in foods:
    print(food["name"], sep=", ")

#Asks which is the food
def food():
    print("What's your food? ")
    choice = input("Qual o seu estudante? ")
    choice = choice.capitalize()
    tell_food(choice)

#Tells Nutrition of the Food
def tell_food(choice):
    if choice == "Maçã":
        print(f"Nome: {foods[0]['name']}, Calorias: {foods[0]['calorias']}, Gordura: {foods[0]['gorduras']}, Carboidratos {foods[0]['carboidratos']}, Proteínas {foods[0]['proteinas']}")
    elif choice =="Banana":
        print(f"Nome: {foods[1]['name']}, Calorias: {foods[1]['calorias']}, Gordura: {foods[1]['gorduras']}, Carboidratos {foods[1]['carboidratos']}, Proteínas {foods[1]['proteinas']}")
    elif choice =="Uva":
        print(f"Nome: {foods[2]['name']}, Calorias: {foods[2]['calorias']}, Gordura: {foods[2]['gorduras']}, Carboidratos {foods[2]['carboidratos']}, Proteínas {foods[2]['proteinas']}")
    elif choice =="Picanha":
        print(f"Nome: {foods[3]['name']}, Calorias: {foods[3]['calorias']}, Gordura: {foods[3]['gorduras']}, Carboidratos {foods[3]['carboidratos']}, Proteínas {foods[3]['proteinas']}")

#Repeats

food()



