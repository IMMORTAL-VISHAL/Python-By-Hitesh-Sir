order_size =input("take a order size of cofee:")

extra_shot = True

if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size +"coffee"

print("Order:",coffee)