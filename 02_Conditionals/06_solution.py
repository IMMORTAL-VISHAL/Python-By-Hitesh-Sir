distance = int(input("give the distance value:"))

if distance<3:
    print("you can walk to cover that distance")
elif distance<15:
    print("you can take bike to cover that distance")
else:
    print("you can take car to cover that distnace because that is too much")