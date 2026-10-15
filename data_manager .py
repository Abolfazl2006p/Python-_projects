import json
def save_data(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f)
        print("data saved successfully!")
    except Exception as e:
        print("Error saving data:", e)
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f) 
    except FileNotFoundError: 
        print("File not found. starting fresh.")
        return {}
    except Exception as e:
        print("Error loading data:", e)
        return {}
data = load_data("data.json")
print("current data:", data)
data["name"] = "Ali"
data["age"] = 20
save_data(data, "data.json")
               