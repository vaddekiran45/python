def calculate_result(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Class"
    elif average >= 50:
        return "Second Class"
    elif average >= 35:
        return "Third Class"
    else:
        return "Fail"

def main():
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")
    marks1 = float(input("Enter marks in subject 1: "))
    marks2 = float(input("Enter marks in subject 2: "))
    marks3 = float(input("Enter marks in subject 3: "))

    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3

    print("\nStudent Result:")
    print("Student Number:", student_number)
    print("Student Name:", student_name)
    print("Total Marks:", total_marks)
    print("Average Marks:", average_marks)
    print("Result:", calculate_result(average_marks))

if _name_ == "_main_":
    main()