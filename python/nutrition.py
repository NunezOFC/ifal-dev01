#shows the foods
foods = [   
    {"name":"Maçã", "calorias":"52kcal", "gorduras":"0,2g", "carboidratos":"14g", "proteinas":"0,3g"},
    {"name":"Banana", "calorias":"89kcal", "gorduras":"0,3", "carboidratos":"23g", "proteinas":"1,1g"},
    {"name":"Uva", "calorias":"67kcal", "gorduras":"0,4g", "carboidratos":"17g", "proteinas":"0,6g"},
    {"name":"Picanha", "calorias":"325kcal", "gorduras":"26,7g", "carboidratos":"0g", "proteinas":"19,72g"},
    {"name":"Frango", "calorias":"239kcal", "gorduras":"14g", "carboidratos":"0g", "proteinas":"27g"},
    {"name":"Bacon", "calorias":"541kcal", "gorduras":"42g", "carboidratos":"1,4g", "proteinas":"37g"},
    {"name":"Bolo de cenoura", "calorias":"359,44kcal", "gorduras":"16,77g", "carboidratos":"47,35g", "proteinas":"4,15g"},
    {"name":"Lasanha", "calorias":"418kcal", "gorduras":"16g", "carboidratos": "33g", "proteinas":"36g"},
    {"name":"Pao com manteiga", "calorias":"426kcal", "gorduras":"25g", "carboidratos":"42,2g", "proteinas":"7,14g"},
    {"name":"Coxinha", "calorias":"117kcal", "gorduras":"4,2g", "carboidratos":"0g", "proteinas":"20g"}
  ]

for  choice_food in foods:
    print(choice_food["name"], sep=", ")

#Asks which is the food
def choice_food():
    print("")
    choice = input("Qual sua comida? ")
    choice = choice.capitalize()
    nutr_food(choice)

#Tells Nutrition of the Food
def nutr_food(choice):
    for food in foods:
        if food["name"] == choice:
            print("Nome:", food["name"],", Calorias: ",food["calorias"], "Gorduras:",food["gorduras"], "Carboidratos:",food["carboidratos"], "Proteinas:",food["proteinas"])
    rep()

#Repeats
def rep():
    print("")
    rep = input("Quer outra comida? (s/n) ")
    if rep == "s":
        choice_food()

choice_food()
