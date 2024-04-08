age = int(input("give the input of age :"))
weekday = input("Take the input of week day: ")

price = 12 if age>=18 else 8

if weekday=="wednesday" :
    price=price-2

print("Ticket price for you is $",price)