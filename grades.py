names = ["Ali", "Reza", "Sara"]
scores = [18, 15, 20]
def show_grades(names, scores):
    for name, score in zip(names, scores):
        if score >= 18:
            status = "Excellent"
        elif score >= 15:
            status = "Good"
        else:
            status = "Needs work"
        print(f"{name}: {score} - {status}")
show_grades(names, scores)
                    