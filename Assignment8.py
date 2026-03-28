import csv

def write_grades():
    """
    Parameters:
        studentamt: integer
        first_name: string
        last_name: string
        grade1: integer
        grade2: integer
        grade3: integer
    Variables:
        studentamt: number of students to enter
        writer: csv writer object
        first_name: student first name
        last_name: student last name
        grade1: first grade
        grade2: second grade
        grade3: third grade

    Logic:
        1. Open csv in write mode
        2. Initialize formatting
        3. Input student/grade data
        4. Loop through student input until studentamt is reached
        5. Write to csv.
    Return:
        None
    """
    studentamt = int(input("How many students would you like to record grades for?: "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        #Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        #For amount of students in studentamt, input student/grades
        for i in range(studentamt):
            print(f"\nEntering data for student {i + 1}:")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            grade1 = int(input(f"Enter the first grade for {first_name}: "))
            grade2 = int(input(f"Enter the second grade for {first_name}: "))
            grade3 = int(input(f"Enter the third grade for {first_name}: "))

            #Write student record
            writer.writerow([first_name, last_name, grade1, grade2, grade3])


#Function 2: Read and display grades
def read_grades():
    """
    Parameters:
        Student name <15 characters
        grades <10 characters

    Variables:
        reader: csv reader object

    Logic:
        1. Open csv in read mode
        2. Initialize formatting
    Return:
        None
    """
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        print("\nStudent Grades:\n")

        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


# Run the program
def main():
    write_grades()
    read_grades()


if __name__ == "__main__":
    main()