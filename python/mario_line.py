#Size Choice
def line():
    print("What's the Line size?")
    size = int(input(""))
    make_line(size)

#Line Maker
def make_line(size):
    while size >0:
        print("🧱", end="")
        size -= 1
    end="\n"

line()
