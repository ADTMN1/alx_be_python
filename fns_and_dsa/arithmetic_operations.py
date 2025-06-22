def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Simple test block
if __name__ == "__main__":
    print("Test Mode: Arithmetic Operations")
    print("5 + 3 =", perform_operation(5, 3, "add"))
    print("5 - 3 =", perform_operation(5, 3, "subtract"))
    print("5 * 3 =", perform_operation(5, 3, "multiply"))
    print("5 / 0 =", perform_operation(5, 0, "divide"))
