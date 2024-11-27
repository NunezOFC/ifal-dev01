result= None
result2 = None 
#Escolha da Expressão
def ex():
    print("Escreva a sua operação/Exemplo (2+1) ")
    ex = input("")
    sep(ex)

#Separação da expressão
def sep(ex):
    ex = ex.replace("+", " + ")
    ex = ex.replace("-", " - ")
    ex = ex.replace("/", " / ")
    ex = ex.replace("**", " ** ")
    ex = ex.replace("*", " * ")
    ex = ex.split()
    size = len(ex)
    if size == 3:
        cal3(ex)
    elif size == 5:
        cal5(ex, size)

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

#Calculus
def cal5(ex):
    if ex[1] == "*":
        result 

ex()
