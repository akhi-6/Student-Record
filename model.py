class Student:
    def __init__(self, roll, name, age, branch):
        self.roll = roll
        self.name = name
        self.age = age
        self.branch = branch
        
class StudentManager:
    FILE_NAME = "data.txt"

    def add_student(self, roll, name, age, branch):
        if self.find_student(roll):
            return False

        with open(self.FILE_NAME, "a") as file:
            file.write(f"{roll},{name},{age},{branch}\n")
        return True

    def get_all_students(self):
        students = []
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        students.append(parts)
        except FileNotFoundError:
            pass
        return students

    def view_students(self):
        students = self.get_all_students()
        if not students:
            print("No student records found.")
            return

        print("\n---- Student Records ----")
        for roll, name, age, branch in students:
            print(f"Roll: {roll} | Name: {name} | Age: {age} | Branch: {branch}")

    def find_student(self, roll_no):
        students = self.get_all_students()
        for roll, _, _, _ in students:
            if roll == roll_no:
                return True
        return False

    def update_student(self, roll_no, updates):
        students = self.get_all_students()
        updated = False

        for student in students:
            if student[0] == roll_no:
                if "roll" in updates:
                    if updates["roll"] != roll_no and self.find_student(updates["roll"]):
                        return False
                    student[0] = updates["roll"]
                if "name" in updates:
                    student[1] = updates["name"]
                if "age" in updates:
                    student[2] = updates["age"]
                if "branch" in updates:
                    student[3] = updates["branch"]
                updated = True

        if updated:
            with open(self.FILE_NAME, "w") as file:
                for student in students:
                    file.write(",".join(student) + "\n")

        return updated

    def delete_student(self, roll_no):
        students = self.get_all_students()
        new_list = [s for s in students if s[0] != roll_no]

        if len(new_list) == len(students):
            return False

        with open(self.FILE_NAME, "w") as file:
            for student in new_list:
                file.write(",".join(student) + "\n")

        return True