import json
def load_grades():
    try:
        with open("grades.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_grades(grades):
    with open("grades.json", "w") as f:
        json.dump(grades, f)
def add_grades(grades):
    name = input("Student name: ")
    score = float(input("Score: "))
    grades[name] = score
    save_grades(grades)
    print("Grade added!")
def show_grades(grades):
    if not grades:
        print("No grades yet.")
        return
    for name. score in grades.items():
        status = "Excellent" if score >= 18 else "Good" if score >= 15 else "Needs work"
        print(f"{name}: {score} - {status}")
def average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)
grades = load_grades()
while True:
    print("\n1. Add  2. show  3. Average  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_grades(grades)
    elif choice == "2":
        print("Average:", average(grades))
    elif choice == "4":
        break
        