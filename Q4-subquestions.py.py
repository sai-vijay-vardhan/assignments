student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

# 1
print(student.get("name"))

# 2
student["grade"] = "A"

# 3
student.update({"age": 22})

# 4
student.pop("age")

# 5
student.popitem()

# 6
print(student.keys())

# 7
print(student.values())

# 8
print(student.items())

# 9
student.setdefault("city", "Hyderabad")

# 10
student.update({"gender": "Male"})