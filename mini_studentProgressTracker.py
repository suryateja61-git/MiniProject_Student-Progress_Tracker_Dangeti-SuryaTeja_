def welcome():
    print("-----------------------------------------")
    print("     STUDENT PROGRESS TRACKER SYSTEM")
    print("-----------------------------------------")

    student_name = input("Enter student name: ").upper()
    student_class = input("Enter student class: ")
    student_rollno = input("Enter student rollno: ")

    subjects = int(input("Enter your subjects: "))

    marks_list = []
    total_marks = 0
    check = True

    for n in range(1, subjects + 1):
        marks = int(input(f"Enter your marks {n}: "))

        if marks < 0 or marks > 100:
            check = False
            print(
                "Invalid marks, Enter marks between 1 to 100. Otherwise you got wrong progress"
            )

        marks_list.append(marks)
        total_marks += marks

    average_marks = float(total_marks / subjects)

    return (
        student_name,
        student_class,
        student_rollno,
        marks_list,
        total_marks,
        average_marks,
    )


def report(
    student_name,
    student_class,
    student_rollno,
    total_marks,
    average_marks,
    grade,
):
    print("--------------------------------------------------")
    print("          STUDENT PROGRESS REPORT")
    print("--------------------------------------------------")
    print(f"Name: --------- {student_name}")
    print(f"Class: -------- {student_class}")
    print(f"Roll No: ------ {student_rollno}")
    print(f"Total: -------- {total_marks}")
    print(f"Average: ------ {average_marks}")
    print(f"Grade: -------- {grade}")


def avg(average_marks):
    if average_marks > 98:
        return "O"
    elif average_marks > 90:
        return "A"
    elif 75 < average_marks <= 89:
        return "B"
    elif 50 < average_marks <= 74:
        return "C"
    elif 35 < average_marks <= 49:
        return "D"
    else:
        return "F"


student_name, student_class, student_rollno, marks_list, total_marks, average_marks = (
    welcome()
)

grade = avg(average_marks)

report(
    student_name,
    student_class,
    student_rollno,
    total_marks,
    average_marks,
    grade,
)

if any(m < 35 for m in marks_list):
    print("Fail")
else:
    print("Pass")

while True:
    print("----------Main Menu----------")
    print("1. Enter Marks Again")
    print("2. View Report Again")
    print("3. Exit")

    user_ip = input("Enter your choice: ")

    if user_ip == "1":
        (
            student_name,
            student_class,
            student_rollno,
            marks_list,
            total_marks,
            average_marks,
        ) = welcome()

        grade = avg(average_marks)

        report(
            student_name,
            student_class,
            student_rollno,
            total_marks,
            average_marks,
            grade,
        )

        if any(m < 35 for m in marks_list):
            print("Fail")
        else:
            print("Pass")

    elif user_ip == "2":
        report(
            student_name,
            student_class,
            student_rollno,
            total_marks,
            average_marks,
            grade,
        )

        if any(m < 35 for m in marks_list):
            print("Fail")
        else:
            print("Pass")

    elif user_ip == "3":
        print("Student Progress Tracked Successfully")
        break

    else:
        print("Enter option 1, 2, or 3")
