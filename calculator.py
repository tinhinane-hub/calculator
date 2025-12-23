while True:  
    print("\nWEErrrlcome to the calculator")
    print("Choose operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("E Exit")

   
    operation = input("Enter the operation (+, -, *, /, E): ")

    
    if operation == 'E': 
        print("Goodbye!")
        break  

    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

   
    if operation == '+':
        result = num1 + num2 + num3
    elif operation == '-':
        result = num1 - num2 - num3
    elif operation == '*':
        result = num1 * num2 * num3
    elif operation == '/':
        if num2 == 0 and num3 == 0:
            print("Error: Division by zero!")
            continue
        else:
             result = num1 / num2 / num3
    else:
        print("Invalid operation!")
        continue  

   
    print("Result:", result)


