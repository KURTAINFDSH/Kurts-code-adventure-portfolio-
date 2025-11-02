# Data storage
students = []
ages = []
birthyears = []

while True:
    register = input("\nType 'Register' to add a student, 'Student list' to view chart, or 'Exit' to quit: ").lower()

    if register == "register":
        try:
            full_name = input("Name: ")
            age = int(input("Age: "))  # Convert to integer
            birth_year = int(input("Birth Year: "))  # Convert to integer
            
            # Append to lists
            students.append(full_name)
            ages.append(age)
            birthyears.append(birth_year)

            print(f"Student Registered: {full_name}, Age: {age}, Birth Year: {birth_year}")
        except ValueError:
            print("Invalid input. Please enter a valid age and birth year.")

    elif register == "student list":
        if not students:
            print("No students have been registered.")
        else:
            print("\nStudent List (Name, Age, Birth Year):\n")
            # Format header
            print(f"{'Name':<15} {'Age':<5} {'Birth Year'}")
            print("-" * 30)  # separator line
            # Format student data
            for i, student in enumerate(students):
                print(f"{students[i]:<15} {ages[i]:<5} {birthyears[i]}")
                
            print("\nStudent Age Chart (Text-Based):")
            # Text-based chart (using asterisks)
            for i, student in enumerate(students):
                print(f"{students[i]}: {'*' * ages[i]} ({ages[i]} years old)")

    elif register == "exit":
        print("Exiting program...")
        break  # Exit the loop