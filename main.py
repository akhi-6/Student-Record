from model import StudentManager

manager = StudentManager()


def get_valid_age():
    while True:
        age = input("Enter Age: ")
        if age.isdigit() and 16 <= int(age) <= 100:
            return age
        print("Invalid age. Enter between 16 and 100.")


while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if not choice.isdigit():
        print("Invalid input.")
        continue

    choice = int(choice)

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = get_valid_age()
        branch = input("Enter Branch: ")

        if manager.add_student(roll, name, age, branch):
            print("Student added successfully.")
        else:
            print("Roll number already exists.")

    elif choice == 2:
        manager.view_students()

    elif choice == 3:
        roll = input("Enter Roll Number to update: ")

        if not manager.find_student(roll):
            print("Student not found.")
            continue

        updates = {}

        print("Press Enter if you don't want to change.")

        new_roll = input("New Roll Number: ")
        if new_roll:
            updates["roll"] = new_roll

        new_name = input("New Name: ")
        if new_name:
            updates["name"] = new_name

        new_age = input("New Age: ")
        if new_age and new_age.isdigit() and 16 <= int(new_age) <= 100:
            updates["age"] = new_age

        new_branch = input("New Branch: ")
        if new_branch:
            updates["branch"] = new_branch

        if updates:
            if manager.update_student(roll, updates):
                print("Student updated successfully.")
            else:
                print("Update failed. Roll number may already exist.")
        else:
            print("No changes made.")

    elif choice == 4:
        roll = input("Enter Roll Number to delete: ")

        if manager.delete_student(roll):
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")