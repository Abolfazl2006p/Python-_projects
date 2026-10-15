names = ["Ali", "Reza", "Sara"]
scores = [18, 15, 20]
for i, name in enumerate(names):
    print(f"{i+1}. {name}")
print("---")
for name, score in zip(names, scores):
    print(f"{name}: {score}")
        