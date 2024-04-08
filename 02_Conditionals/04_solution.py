fruit = input("Give the name of fruit:")
color = input("give the color of fruit:")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
else:
    print("So i don't have the info about that fruit.")