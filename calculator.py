def safe_eval(expression):
    """
    Safely evaluate a mathematical expression.
    Only allows basic math operations and numbers.
    """
    allowed_chars = set('0123456789+-*/(). ')
    if not all(c in allowed_chars for c in expression):
        raise ValueError("Invalid characters in expression")

    try:
        result = eval(expression, {"__builtins__": {}})
        return result
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

def main():
    print("Simple Calculator")
    print("Enter mathematical expressions (e.g., 2 + 3 * 4)")
    print("Type 'quit' to exit")

    while True:
        try:
            equation = input("Enter equation: ").strip()
            if equation.lower() == 'quit':
                break
            result = safe_eval(equation)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()