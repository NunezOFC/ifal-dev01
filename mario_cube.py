#Escolha do tamanho
def size_cube():
    print("What's the Cube size?")
    size = int(input(""))
    cube(size)

def cube(size):
    while size > 0:
        print("#", end=(""))
        size -=1

size_cube()
