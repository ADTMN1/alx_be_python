user1=int(input("Enter the first number"))
user2=int(input("Enter the second number"))
choice=(input("Choose the operation (+, -, *, /)"))
if choice=="+":
    print(f"The result is {user1 + user2}")
elif choice=="-":
    print(f"the result is {user1 - user2}")
elif choice=="/":
    if user2==0:
        print("can not divide by zero")
    else:
        print(f"the result is {user1 / user2}")
elif choice=="*":
    print(f"the result is {user1 * user2}")