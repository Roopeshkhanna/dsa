import random
def sorting_descending(students):
    for i in range(1, len(students)):
        j = i
        while j > 0 and (students[j][1] > students[j - 1][1] or (students[j][1] == students[j - 1][1] and students[j][4] > students[j - 1][4])):
            students[j], students[j - 1] = students[j - 1], students[j]
            j -= 1

   

# Define college capacities
college_capacity = {
    "psg": {"IT": 10, "CSE": 10, "ECE": 10},
    "anna": {"IT": 8, "CSE": 6, "ECE": 15},
    "ssn": {"IT": 10, "CSE": 10, "ECE": 10},
    "skcet": {"IT": 15, "CSE": 10, "ECE": 10}
}

students = []

# Number of students
n = int(input("Enter the number of students: "))

# Collect student information
for i in range(n):
    name = input("Enter name: ")
    cutoff = float(input("Enter cutoff [maths+(chem+phy)/2]: "))
    dob = input("Enter DOB: ")
    print("Enter 5 choices (college department)")
    preferences = input("Enter the preferences separated by comma (e.g., psg IT, anna CSE): ").split(',')
    # Generate a random rank for the student
    rank = random.randint(1, n)
    students.append([name, cutoff, dob, preferences, rank])

# Sort students based on cutoff and rank
sorting_descending(students)
    

# Allocation
allocated_students = []
for student in students:
    name, cutoff, dob, preferences, rank = student
    for preference in preferences:
        college, department = preference.strip().split()
        if college in college_capacity and department in college_capacity[college] and college_capacity[college][department] > 0:
            print("Allocated", name, "to", college, department)
            college_capacity[college][department] -= 1
            allocated_students.append(student)
            break
    else:
        print("Not allocated", name)

# Print remaining seats
for college, departments in college_capacity.items():
    for department, seats in departments.items():
        if seats > 0:
            print("Remaining seats in", college, department, ":", seats)
