### 🧮 Math Interpreter

A simple Python program that acts as a mini math interpreter. It prompts the user for an arithmetic expression in the form **x y z** (e.g., `3 * 4`) and outputs the result as a floating-point number rounded to one decimal place.

Supports **addition (+)**, **subtraction (-)**, **multiplication (*)**, and **division (/)** with error handling for invalid input and division by zero.
Includes **pytest** tests in `test_interpreter.py` to verify that all operations produce accurate results.


### 🧪 How to Test

#### Manual Testing

Run the program with:

```bash
python interpreter.py
```

Then test with these examples:

| Input    | Expected Output |
| -------- | --------------- |
| `1 + 1`  | `2.0`           |
| `2 - 3`  | `-1.0`          |
| `2 * 2`  | `4.0`           |
| `50 / 5` | `10.0`          |

#### Automated Testing

Run the tests with **pytest**:

```bash
pytest test_interpreter.py
```

This will automatically check that the `calculate()` function correctly handles all four arithmetic operations and returns floating-point results with one decimal place.
