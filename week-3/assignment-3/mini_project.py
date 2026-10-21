# Mini Project - Day Planner

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "monday":
    if time == "morning":
        print("Suggestion: Start your day with a workout.")
    elif time == "afternoon":
        print("Suggestion: Study Python for one hour.")
    elif time == "evening":
        print("Suggestion: Watch a movie and relax.")

elif day == "friday":
    if time == "morning":
        print("Suggestion: Have a nice breakfast.")
    elif time == "afternoon":
        print("Suggestion: Go for a walk outside.")
    elif time == "evening":
        print("Suggestion: Have dinner with your family.")

elif day == "sunday":
    if time == "morning":
        print("Suggestion: Sleep a little longer.")
    elif time == "afternoon":
        print("Suggestion: Go shopping.")
    elif time == "evening":
        print("Suggestion: Prepare for the next week.")

else:
    print("Sorry, I don't recognize that day.")

if time not in ["morning", "afternoon", "evening"]:
    print("Sorry, I don't recognize that time.")