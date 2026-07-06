# Count the number of students
numofstudents = int(input("Enter Total Students: "))

# Data Storage
studentData = []

# Inserting Data
for i in range(numofstudents):
    print(f"\nEnter the data of student {i+1}")
    name = input("name :")
    roll_no = int(input("roll number :"))
    marks = int(input("marks :"))

    if marks > 95:
        grade = "A"
    elif marks > 80:
        grade = "B"
    elif marks > 60:
        grade = "C"
    elif marks > 33:
        grade = "D"
    else:
        grade = "F"


    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    }
    
    studentData.append(students)

# Data printing
print("\nStudent who are passed: ")

for s in studentData:
    if s["marks"] >= 33:
        print(f"{s['name']} - marks: {s['marks']}")