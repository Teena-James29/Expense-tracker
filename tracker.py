def add():
    c = input("Category: ")
    p = input("Price: ")
    d = input("Date: ")
    f = open("expenses.txt", "a")
    f.write(c + " " + p + " " + d + "\n")
    f.close()

def view():
    f = open("expenses.txt", "r")
    print(f.read())


def total():
    f = open("expenses.txt", "r")
    t = 0
    for line in f:
        t = t + int(line.split()[1])
    print("Total:", t)

while True:
    print("1.Add  2.View  3.Total  4.Exit")
    ch = input("Choice: ")
    if ch == "1": add()
    elif ch == "2": view()
    elif ch == "3": total()
    elif ch == "4": break