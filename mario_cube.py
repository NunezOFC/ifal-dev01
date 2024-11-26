#Size Choice
def cube():
    print("What's the Cube size?")
    size = int(input(""))
    make_cube(size)

#Fazedor de Cubo
def make_cube(size):
    cube = size
    while size > 0:
        print("🟪" * cube)
        size -=1

cube()
