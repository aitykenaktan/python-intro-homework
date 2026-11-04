students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis", "score": 74, "subject": "Data"},
    {"name": "Sara", "score": 91, "subject": "Python"},
    {"name": "Marcus", "score": 68, "subject": "Web"},
    {"name": "Priya", "score": 95, "subject": "Data"},
    {"name": "Devon", "score": 72, "subject": "Python"},
    {"name": "Mia", "score": 83, "subject": "Web"},
    {"name": "Eli", "score": 79, "subject": "Data"}
]

highest_score = 0
top_scorer = ""

total_score = 0
subjects = set()
high_scorers = []

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_scorer = student["name"]

    total_score += student["score"]

    subjects.add(student["subject"])

    if student["score"] > 75:
        high_scorers.append(student["name"])

average = total_score / len(students)

print("Top scorer:", top_scorer, "(", highest_score, ")")
print("Class average:", round(average, 2))
print("Subjects offered:", subjects)
print("High scorers:", high_scorers)