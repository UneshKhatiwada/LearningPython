studentsName = {
    "Alice": 85,
    "Bob": 76,
    "Charlie": 95,
    "Diana": 58
}

# Function to determine grade based on score
def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 50 <= score < 60:
        return "E"
    else:
        return "Fail"

# Assign grades to each student
for student, score in studentsName.items():
    grade = get_grade(score)
    print(f"{student} scored {score} and their grade is {grade}")
