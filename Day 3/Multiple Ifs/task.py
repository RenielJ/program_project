print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $12.")
        bill = 12
    want_photo = input("Do you want a photo? (Y/N)")
    if want_photo == "Y" or want_photo == "y":
        print("Please pay addition $2.")
        bill += 2
    elif want_photo == "N" or want_photo == "n":
        print(f"Your total bill is ${bill}.")
    else:
        print(f"That's not a valid option.")

    print(f"Your total bill is ${bill}.")


else:
    print("Sorry you have to grow taller before you can ride.")
