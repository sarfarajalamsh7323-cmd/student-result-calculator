student_name = input("Enter student name: ")

marks1 = int(input("Enter Maths marks: "))
marks2 = int(input("Enter Python marks: "))
marks3 = int(input("Enter English marks: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("Student:", student_name)
print("Total:", total)
print("Percentage:", percentage)
