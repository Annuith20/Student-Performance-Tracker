import csv
import matplotlib.pyplot as plt
import numpy as np

class Student:
    def __init__(self, name, roll_no, grades):
        self.name = name
        self.roll_no = roll_no
        self.grades = grades

def read_students_data_from_csv(filename):
    students_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            name = row[0]
            roll_no = int(row[1])
            grades = list(map(float, row[2:]))
            student = Student(name, roll_no, grades)
            students_data.append(student)
    return students_data

def calculate_average_grade(grades):
    total_grades = sum(grades)
    return total_grades / len(grades)

def calculate_passing_percentage(students_data):
    total_students = len(students_data)
    passing_students = sum(1 for student in students_data if all(grade >= 40 for grade in student.grades))
    return (passing_students / total_students) * 100

def calculate_top_performer(students_data):
    top_student = max(students_data, key=lambda student: sum(student.grades))
    return top_student

def calculate_average_grade_by_subject(students_data):
    num_subjects = len(students_data[0].grades)
    avg_grades_by_subject = [0] * num_subjects

    for student in students_data:
        for i, grade in enumerate(student.grades):
            avg_grades_by_subject[i] += grade

    for i in range(num_subjects):
        avg_grades_by_subject[i] /= len(students_data)

    return avg_grades_by_subject

def generate_subject_wise_report(students_data):
    subject_names = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
    avg_grades_by_subject = calculate_average_grade_by_subject(students_data)

    print("Subject-wise Report:")
    print("--------------------")

    for i, subject_name in enumerate(subject_names):
        print(f"{subject_name}: Average Grade = {avg_grades_by_subject[i]:.2f}")

def generate_grade_distribution_chart(students_data):
    grades = [grade for student in students_data for grade in student.grades]
    bins = np.arange(0, 101, 10)
    plt.hist(grades, bins=bins, edgecolor='black')
    plt.xticks(bins)
    plt.xlabel('Grades')
    plt.ylabel('Number of Subjects')
    plt.title('Grade Distribution')

    
    plt.ylim(0, 10)
    plt.show()

def generate_average_grade_vs_rollno_chart(students_data):
    roll_numbers = [student.roll_no for student in students_data]
    average_grades = [calculate_average_grade(student.grades) for student in students_data]

    plt.bar(roll_numbers, average_grades)
    plt.xlabel('Student Number')
    plt.ylabel('Average Grade')
    plt.title('Average Grade for each Student')
    plt.xticks(roll_numbers)
    plt.grid(axis='y')
    plt.show()

def sort_students_by_average_grade(students_data):
    return sorted(students_data, key=lambda student: calculate_average_grade(student.grades), reverse=True)

def filter_students_by_subject_grade(students_data, subject_index, min_grade):
    filtered_students = []
    for student in students_data:
        if student.grades[subject_index] >= min_grade:
            filtered_students.append(student)
    return filtered_students

def print_student_details(student):
    average_grade = calculate_average_grade(student.grades)
    status = "Pass" if all(grade >= 40 for grade in student.grades) else "Fail"
    print(f"{student.name} (Roll No. {student.roll_no}):")
    print(f"Grades: {', '.join(map(str, student.grades))}")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Status: {status}")
    print()

def generate_subject_average_chart(students_data):
    subject_names = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
    avg_grades_by_subject = calculate_average_grade_by_subject(students_data)

    plt.bar(subject_names, avg_grades_by_subject)
    plt.xlabel('Subjects')
    plt.ylabel('Average Grade')
    plt.title('Average Grade for Each Subject')
    plt.ylim(0, 100) 
    plt.grid(axis='y')
    plt.show()

if __name__ == '__main__':
    filename = "students_data.csv"
    students_data = read_students_data_from_csv(filename)

    # Additional data processing and analysis tasks
    sorted_students = sort_students_by_average_grade(students_data)
    physics_passed_students = filter_students_by_subject_grade(students_data, 0, 40)
    top_5_students = sorted_students[:5]

    # Additional output
    print("Top 5 Students:")
    print("----------------")
    for student in top_5_students:
        print_student_details(student)

    # Generate the grade distribution chart
    generate_grade_distribution_chart(students_data)
    generate_average_grade_vs_rollno_chart(students_data)
    generate_subject_average_chart(students_data)
    generate_subject_wise_report(students_data)

    # Display the chart
    plt.show()
