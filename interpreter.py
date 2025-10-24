def main():
    print("Example: 2 + 2")

    while True:
        expression = input("Expression: ").strip()

        try:
            x, operator, z = expression.split(" ")
            x = int(x)
            z = int(z)

            # handle zero division safely
            if operator == "/" and z == 0:
                raise ZeroDivisionError("Cannot divide by zero!")

            result = calculate(x, operator, z)
            print(f"Result: {result: .1f}")
            break  # only break when successful

        except ValueError:
            print("Invalid input. Please enter in the format: number operator number")
        except ZeroDivisionError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


def calculate(x, operand, z):
    if operand == "+":
        return x + z
    elif operand == "-":
        return x - z
    elif operand == "/":
        return x / z
    elif operand == "*":
        return x * z
    else:
        raise ValueError("Invalid operand. Use +, -, *, or /.")


if __name__ == "__main__":
    main()
