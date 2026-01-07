  CGPA Calculator in Python

# Create a grade-to-point mapping
grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "F": 1,
}

# Get number of courses
num_courses = int(input("Enter number of courses: "))

total_weighted_points = 0
total_credits = 0

#  Loop through each course
for i in range(num_courses):
    course_name = input(f"Enter name of course {i+1}: ")
    credit = float(input(f"Enter credit units for {course_name}: "))
    grade = input(f"Enter grade for {course_name} (A-F): ").upper()
    
    # Calculate weighted points
    if grade in grade_points:
        total_weighted_points += credit * grade_points[grade]
        total_credits += credit
    else:
        print("Invalid grade entered, skipping this course.")

# Calculate CGPA
if total_credits == 0:
    print("No valid credits entered. CGPA cannot be calculated.")
else:
    cgpa = total_weighted_points / total_credits
    print(f"Your CGPA is: {cgpa:}")

