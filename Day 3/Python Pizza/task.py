print("Welcome to Python Pizza Deliveries!")

bill = 0
size = input("What size pizza do you want? type S for small, M for medium or L for large: ")
pepperoni = input("Do you want pepperoni on your pizza? type Y for yes and N for no: ")
extra_cheese = input("Do you want extra cheese? type Y for yes and N for no: ")
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")

else:
    print("Sorry, please enter S, M, or L")


