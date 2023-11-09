import re

def perform_operation(match):
    operator = match.group(2)
    num1 = float(match.group(1))
    num2 = float(match.group(3))
   
    if operator == '+':
        return str(num1 + num2) 
    elif operator == '-':
        return str(num1 - num2)  
    elif operator == '*':
        return str(num1 * num2)  
    elif operator == '/':
        return str(num1 / num2)  
    elif operator == '**':
        return str(num1 ** num2)  


def calculate(expression):
    while '(' in expression:
        # Find the innermost expression in parentheses
        innermost_expr = re.search(r'\(([^()]+)\)', expression)
        if innermost_expr:
            result = calculate(innermost_expr.group(1))
            expression = expression.replace(innermost_expr.group(0), str(result))
        else:
            break

    # Perform calculations following BODMAS
    while re.search(r'[\+\-\*\/\*\*]', expression):
        expression = re.sub(r'(\d+\.*\d*)\s*([\+\-\*\/\*\*])\s*(\d+\.*\d*)', perform_operation, expression)

    try:
        result = float(expression)
        return result
    except:
        return "Error"

def main():
    print("Welcome to the Python Calculator!")
    expression = input("Enter an expression: ")
    result = calculate(expression)
    print("Result:", result)

if __name__ == "__main__":
    main()
