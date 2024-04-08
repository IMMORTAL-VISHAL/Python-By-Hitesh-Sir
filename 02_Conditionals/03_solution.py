score = int(input("Enter the number of points you scored: "))

if score>=101 :
    print("Give the right number you scored:")
    exit()

if score>=90:
    grade = "A"
if score>=80:
    grade = "B"
if score>=70:
    grade = "C"
if score>=60:
    garde = "D"
else:
    grade = "E"

print("Your grade is :",grade)