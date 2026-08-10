# Day 19 - Set Operations
# Name: Thanush B G

python_students = {"Thanush", "Arjun","Rahul","Meera"}
java_students = {"Rahul", "Meera"," Vishnu","Arjun"}

# Intersection - students in both sets
both = python_students & java_students
print(both)

# Union - students from both sets
all_students = python_students | java_students
print(all_students)

# Difference - Python student but not Java students
python_only = python_students - java_students
print(python_only)

# Difference - Java students but not python students
java_only = java_students - python_students
print(java_only)