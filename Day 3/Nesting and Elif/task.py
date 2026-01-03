print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    age = int(input("What is your age? "))
    if age >= 18:
        print("Please pay $12.")
        sure = input("Are you already paid $12? (Y/N)")
        if sure == "Y" or sure == "y":
            print("You can ride the rollercoaster!")
        elif sure == "N" or sure == "n":
            print("Sorry, you cannot ride the rollercoaster!")
        else:
            print("That's not a valid option!")
    elif age >= 12:
        print("Please pay $7.")
        sure = input("Are you already paid $7? (Y/N)")
        if sure == "Y" or sure == "y":
            print("You can ride the rollercoaster!")
        elif sure == "N" or sure == "n":
            print("Sorry, you cannot ride the rollercoaster!")
        else:
            print("That's not a valid option!")
    else:
        print("Please pay $5.")
        sure = input("Are you already paid $5? (Y/N)")
        if sure == "Y" or sure == "y":
            print("You can ride the rollercoaster!")
        elif sure == "N" or sure == "n":
            print("Sorry, you cannot ride the rollercoaster!")
        else:
            print("That's not a valid option!")
else:
    print("Sorry you have to grow taller before you can ride.")
