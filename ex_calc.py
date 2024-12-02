result= None
result2 = None 
#Escolha da Expressão
def ex():
    print("Use * para multiplicaçao e ** para exponenciaçao")
    print("")
    print("Escreva a sua operação/Exemplo (2+1) ")
    ex = input("")
    sep(ex)

#Separação da expressão
def sep(ex):
    ex = ex.replace("+", " + ")
    ex = ex.replace("-", " - ")
    ex = ex.replace("/", " / ")
    ex = ex.replace("**", " ^ ")
    ex = ex.replace("*", " * ")
    ex = ex.split()
    size = len(ex)
    if size == 3:
        cal3(ex)
    elif size == 5:
        cal5(ex)

#Calculus
def cal3(ex):
    if ex[1] == "+":
        result = float(ex[0]) + float(ex[2])
        print(f"The result of {ex[0]} + {ex[2]} = {result}")
    elif ex[1] == "-":
        result = float(ex[0]) - float(ex[2])
        print(f"The result of {ex[0]} - {ex[2]} = {result}")
    elif ex[1] == "*":
        result = float(ex[0]) * float(ex[2])
        print(f"The result of {ex[0]} x {ex[2]} = {result}")
    elif ex[1] == "/":
        result = float(ex[0]) / float(ex[2])
        print(f"The result of {ex[0]} / {ex[2]} = {result}")
    elif ex[1] == "^":
        result = float(ex[0]) ** float(ex[2])
        print(f"The result of {ex[0]} ^ {ex[2]} = {result}")

#Calculus
def cal5(ex):
    if ex[3] == "^":
        result = float(ex[2]) ** float(ex[4])
        if ex[1] == "+":
            result2 = float(result) + float(ex[0])
            print(f"The result of {ex[0]} + {ex[2]} ^ {ex[4]} = {result2}")
        elif ex[1] == "-":
            result2 = float(result) - float(ex[0])
            print(f"The result of {ex[0]} - {ex[2]} ^ {ex[4]} = {result2}")
        elif ex[1] == "*":
            result2 = float(result) * float(ex[0])
            print(f"The result of {ex[0]} x {ex[2]} ^ {ex[4]} = {result2}")
        elif ex[1] == "/":
            result2 = float(result) / float(ex[0])
            print(f"The result of {ex[0]} / {ex[2]} ^ {ex[4]} = {result2}")
        elif ex[1] == "^":
            result2 = float(result) ** float(ex[0])
            print(f"The result of {ex[0]} ^ {ex[2]} ^ {ex[4]} = {result2}")
    elif ex[1] == "^":
        result = float(ex[0]) ** float(ex[2])
        if ex[3] == "+":
            result2 = float(result) + float(ex[4])
            print(f"The result of {ex[0]} ^ {ex[2]} + {ex[4]} = {result2}")
        elif ex[3] == "-":
            result2 = float(result) - float(ex[4])
            print(f"The result of {ex[0]} ^ {ex[2]} - {ex[4]} = {result2}")
        elif ex[3] == "*":
            result2 = float(result) * float(ex[4])
            print(f"The result of {ex[0]} ^ {ex[2]} * {ex[4]} = {result2}")
        elif ex[3] == "/":
            result2 = float(result) / float(ex[4])
            print(f"The result of {ex[0]} ^ {ex[2]} / {ex[4]} = {result2}")
    elif ex[1] == "*":
        result = float(ex[0]) * float(ex[2])
        if ex[3] == "+":
            result2 = float(result) + float(ex[4])
            print(f"The result of {ex[0]} x {ex[2]} + {ex[4]} = {result2}")
        elif ex[3] == "-":
            result2 = float(result) - float(ex[4])
            print(f"The result of {ex[0]} x {ex[2]} - {ex[4]} = {result2}")
        elif ex[3] == "*":
            result2 = float(result) * float(ex[4])
            print(f"The result of {ex[0]} x {ex[2]} * {ex[4]} = {result2}")
        elif ex[3] == "/":
            result2 = float(result) / float(ex[4])
            print(f"The result of {ex[0]} x {ex[2]} / {ex[4]} = {result2}")
    elif ex[1] == "/":
        result = float(ex[0]) / float(ex[2])
        if ex[3] == "+":
            result2 = float(result) + float(ex[4])
            print(f"The result of {ex[0]} / {ex[2]} + {ex[4]} = {result2}")
        elif ex[3] == "-":
            result2 = float(result) - float(ex[4])
            print(f"The result of {ex[0]} / {ex[2]} - {ex[4]} = {result2}")
        elif ex[3] == "*":
            result2 = float(result) * float(ex[4])
            print(f"The result of {ex[0]} / {ex[2]} * {ex[4]} = {result2}")
        elif ex[3] == "/":
            result2 = float(result) / float(ex[4])
            print(f"The result of {ex[0]}  {ex[2]} / {ex[4]} = {result2}")

ex()
