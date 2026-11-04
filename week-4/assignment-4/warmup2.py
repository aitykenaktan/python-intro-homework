student = {
    "name": "Almaz",
    "grade": 88,
    "subjects": ["Computer Science", "Biology", "Chemistry"]
}

for key, value in student.items():
    print(key, ":", value)

student["graduated"] = False

print("Updated dictionary:", student)