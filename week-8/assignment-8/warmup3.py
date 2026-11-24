try:
    with open("../data/missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! File not found. Please check the file name.")