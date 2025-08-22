from student_db import create_table, add_student, view_students, update_student, delete_student

def main():
    create_table()

    while True:
        print("\nStudent Database")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            add_student(name, age, course)
            print("Student added!")

        elif choice == "2":
            students = view_students()
            print("\nID | Name | Age | Course")
            print("-"*30)
            for s in students:
                print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]}")

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            update_student(student_id, name, age, course)
            print("Student updated!")

        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
            print("🗑️ Student deleted!")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
