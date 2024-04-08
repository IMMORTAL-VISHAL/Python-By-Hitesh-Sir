pet_type = input("give the pet type")
pet_age = int(input("Give the pet age :"))

if (pet_type=="dog" and pet_age<2) :
    print("This is demand the puppy food")
elif (pet_type=="cat" and pet_age >5):
    print("This is demand a senior cat food")
else:
    print("The input is given by you is not fit there.Please try again")