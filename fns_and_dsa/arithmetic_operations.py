num1 = float(input("num1: "))
num2 = float(input("num2: "))
operation = input("operation: ")

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
            return result
        case 'subtract':
            result = num1 - num2
            return result
        case 'divide':
            if num2 == 0:
                return num1
            elif num2 != 0:
                result = num1 / num2
            return result
        case 'multiply':
            result = num1 * num2
            return result 
        case _:
            print("invalid operation")
            return 1