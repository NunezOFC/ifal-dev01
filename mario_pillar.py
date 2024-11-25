#Escolha do tamanho
def size_pillar():
    print("What's the Pillar size?")
    size = int(input(""))
    pillar(size)

def pillar(size):
    while size >0:
        print("#")
        size -= 1

size_pillar()