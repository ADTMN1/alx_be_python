user1 = int(input("Enter the first number: "))
user2 = int(input("Enter the second number: "))
choice = input("Choose the operation (+, -, *, /): ")

if choice == "+":
    print(f"The result is {user1 + user2}")
elif choice == "-":
    print(f"The result is {user1 - user2}")
elif choice == "/":
    if user2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"The result is {user1 / user2}")
elif choice == "*":
    print(f"The result is {user1 * user2}")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
