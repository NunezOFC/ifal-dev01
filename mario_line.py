#Escolha do tamanho
def size_line():
    print("What's the Pillar size?")
    size = int(input(""))
    line(size)

def line(size):
    while size >0:
        print("?", end="")
        size -= 1

size_line()