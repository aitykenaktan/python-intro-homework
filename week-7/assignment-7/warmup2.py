import csv

with open("../data/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(f"{student['name']}: {student['score']}")