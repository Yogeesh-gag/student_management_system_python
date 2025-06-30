# Dictionary to store student records with roll number as key
students = {}

# Infinite loop to keep the menu running until user exits
while True:
    # Display the main menu
    print("\n-----------Student Management System-----------")
    print("1. Add Student")
    print("2. View Student")  
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    # Get user's choice
    choice = input("Enter your choice (1-5): ")

    # Option 1: Add new student
    if choice == '1':
        roll_number = input("Enter roll number (alphanumeric): ")
        if roll_number in students:
            print("Student with this roll number already exists.")
            continue  # Skip rest of the loop if roll number already exists

        name = input("Enter name (alphabets only): ")
        if not name.isalpha():  # Validate that name contains only alphabets
            print(f"{name} is invalid. Only alphabets allowed.")
            continue

        age = input("Enter age (digits only): ")
        if not age.isdigit():  # Validate that age is numeric
            print("Invalid age. Only digits allowed.")
            continue

        marks = input("Enter marks (float): ")
        # Validate marks as a float value
        if '.' not in marks or not marks.replace('.', '', 1).isdigit():
            print("Invalid marks. Must be float value.")
            continue

        marks = float(marks)  # Convert marks to float

        # Grade calculation based on marks
        if marks >= 90.0:
            grade = 'A'
        elif marks >= 75.0:
            grade = 'B'
        elif marks >= 60.0:
            grade = 'C'
        elif marks >= 45.0:
            grade = 'D'
        else:
            grade = 'F'

        # Save student data to the dictionary
        students[roll_number] = {
            "name": name,
            "age": int(age),
            "marks": marks,
            "grade": grade
        }

        print("Student added successfully.\n")

    # Option 2: View all student records
    elif choice == '2':
        if len(students) == 0:
            print("No student records found...")
        else:
            # Loop through each student and print their info
            for roll_number, info in students.items():
                print(f"\nRoll Number: {roll_number}")
                print(f"Name: {info['name']}")
                print(f"Age: {info['age']}")
                print(f"Marks: {info['marks']}")
                print(f"Grade: {info['grade']}")

    # Option 3: Update an existing student
    elif choice == '3':
        roll_number = input("Enter Roll Number to update: ")
        if roll_number not in students:
            print("Student not found...")
        else:
            print("Leave blank to keep current value.")

            name = input("Enter new name: ")
            if name != "" and not name.isalpha():
                print("Invalid name.")
                continue

            age = input("Enter new age: ")
            if age != "" and not age.isdigit():
                print("Invalid age.")
                continue

            marks = input("Enter new marks: ")
            if marks != "" and ('.' not in marks or not marks.replace('.', '', 1).isdigit()):
                print("Invalid marks.")
                continue

            # Update values only if input is not blank
            if name != "":
                students[roll_number]["name"] = name
            if age != "":
                students[roll_number]["age"] = int(age)
            if marks != "":
                marks = float(marks)
                students[roll_number]["marks"] = marks

                # Recalculate grade based on updated marks
                if marks >= 90.0:
                    grade = 'A'
                elif marks >= 75.0:
                    grade = 'B'
                elif marks >= 60.0:
                    grade = 'C'
                elif marks >= 45.0:
                    grade = 'D'
                else:
                    grade = 'F'
                students[roll_number]["grade"] = grade

            print("Student record updated successfully.")

    # Option 4: Delete a student record
    elif choice == '4':
        roll_number = input("Enter Roll number to delete: ")
        if roll_number in students:
            del students[roll_number]  # Remove student from dictionary
            print("Student record deleted successfully.")
        else:
            print("Student record not found.")

    # Option 5: Exit the program
    elif choice == '5':
        print("👋 Exiting... Thank you!")
        break  # Exit the loop and end the program

    # If user enters invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 to 5.")
