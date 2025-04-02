#Asks you to write a Number
def main():
    num = int(input("Write a Number: "))
    if pair_calculator(num):
        print("Pair")
    else:
        print("Unpaired")

#Verifys if the number is Pair
def pair_calculator(num):
    return num % 2 == 0

main()
