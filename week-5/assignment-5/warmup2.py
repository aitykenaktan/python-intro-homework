while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number > 0:
            break
        else:
            print("That's not a positive integer. Try again.")

    except ValueError:
        print("Invalid input. Try again.")

print("Got it:", number)