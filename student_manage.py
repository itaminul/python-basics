students = []
while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Save ")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        students.append({'name': name, 'age': age})
        print(f"Student {name} added successfully.")

    elif choice == '2':
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}")
    elif choice == '3':
        with open('students.txt', 'w') as f:
            for student in students:
                f.write(f"{student['name']},{student['age']}\n")
        print("Students saved to students.txt.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")