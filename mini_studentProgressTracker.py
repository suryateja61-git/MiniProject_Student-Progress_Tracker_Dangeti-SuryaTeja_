```python
def welcome():
    print("\n" + "=" * 50)
    print("      STUDENT PROGRESS TRACKER SYSTEM")
    print("=" * 50)

    student_name = input("Enter Student Name: ").upper()
    student_class = input("Enter Student Class: ")
    student_rollno = input("Enter Student Roll No: ")

    subjects = int(input("Enter Number of Subjects: "))

    marks_list = []
    total_marks = 0

    for i in range(1, subjects + 1):

        while True:
            marks = int(input(f"Enter Marks for Subject {i}: "))

            if 0 <= marks <= 100:
                break

            print("Invalid Marks! Enter marks between 0 and 100.")

        marks_list.append(marks)
        total_marks += marks

    average_marks = total_marks / subjects

    return (
        student_name,
        student_class,
        student_rollno,
        marks_list,
        total_marks,
        average_marks,
    )


def calculate_grade(avg):
    if avg >= 98:
        return "O"
    elif avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 35:
        return "D"
    else:
        return "F"


def get_result(marks_list):
    if any(mark < 35 for mark in marks_list):
        return "FAIL"
    return "PASS"


def report(
    student_name,
    student_class,
    student_rollno,
    marks_list,
    total_marks,
    average_marks,
    grade,
    result,
):
    print("\n" + "=" * 50)
    print("           STUDENT PROGRESS REPORT")
    print("=" * 50)

    print(f"Name      : {student_name}")
    print(f"Class     : {student_class}")
    print(f"Roll No   : {student_rollno}")

    print("\nSubject-wise Marks")

    for i, mark in enumerate(marks_list, start=1):
        print(f"Subject {i}: {mark}")

    print("-" * 50)

    print(f"Total Marks : {total_marks}")
    print(f"Average     : {average_marks:.2f}")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")

    print("=" * 50)


# First Entry
student_name, student_class, student_rollno, marks_list, total_marks, average_marks = welcome()

grade = calculate_grade(average_marks)
result = get_result(marks_list)

report(
    student_name,
    student_class,
    student_rollno,
    marks_list,
    total_marks,
    average_marks,
    grade,
    result,
)

# Menu
while True:

    print("\nMAIN MENU")
    print("1. Enter New Student")
    print("2. View Current Report")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        (
            student_name,
            student_class,
            student_rollno,
            marks_list,
            total_marks,
            average_marks,
        ) = welcome()

        grade = calculate_grade(average_marks)
        result = get_result(marks_list)

        report(
            student_name,
            student_class,
            student_rollno,
            marks_list,
            total_marks,
            average_marks,
            grade,
            result,
        )

    elif choice == "2":

        report(
            student_name,
            student_class,
            student_rollno,
            marks_list,
            total_marks,
            average_marks,
            grade,
            result,
        )

    elif choice == "3":
        print("\nStudent Progress Tracked Successfully!")
        break

    else:
        print("Invalid Choice! Please enter 1, 2, or 3.")
```
