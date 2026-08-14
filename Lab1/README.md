# Lab 1 – Python Basics

## variable_practice.py
- **Aim:** Declare variables for name, age, height, and student status, and print each with its type.
- **Logic:** Assign four values of different types (str, int, float, bool) to variables, then use `type()` inside `print()` to show each one's data type.
- **Sample Output:**
  ```
  Ravi Kumar -> <class 'str'>
  20 -> <class 'int'>
  5.9 -> <class 'float'>
  True -> <class 'bool'>
  ```

## greeting.py
- **Aim:** Take a user's name, age, and city and print one combined greeting sentence.
- **Logic:** Read three values with `input()`, then use an f-string to embed all three directly into one sentence.
- **Sample Input:** `Ravi`, `20`, `Bhilai`
- **Sample Output:** `Hi Ravi, you are 20 years old and you live in Bhilai.`

## arithmetic.py
- **Aim:** Take two numbers and print their sum, difference, product, quotient, and remainder.
- **Logic:** Convert both inputs to `float` so decimals work too, then apply `+ - * / %` and print each labeled result.
- **Sample Input:** `10`, `3`
- **Sample Output:**
  ```
  Sum: 13.0
  Difference: 7.0
  Product: 30.0
  Quotient: 3.3333333333333335
  Remainder: 1.0
  ```

## celsius_to_fahrenheit.py
- **Aim:** Convert a Celsius temperature to Fahrenheit.
- **Logic:** Read the Celsius value, convert to `float`, apply the formula `F = (C * 9/5) + 32`, and print the result.
- **Sample Input:** `37`
- **Sample Output:** `37.0°C is equal to 98.6°F`

## string_manipulation.py
- **Aim:** Take a full name and print it uppercase, lowercase, reversed, and its length.
- **Logic:** Read the name and clean it with `.strip()`, then apply `.upper()` and `.lower()`, reverse it with slice `[::-1]`, and get length with `len()`.
- **Sample Input:** `Ravi Kumar`
- **Sample Output:**
  ```
  Uppercase: RAVI KUMAR
  Lowercase: ravi kumar
  Reversed: ramuK ivaR
  Length: 10
  ```

## escape_sequence.py
- **Aim:** Print a small receipt-style layout using tabs and newlines.
- **Logic:** Use `\t` between item name and price to align columns, and `\n` to separate rows and add spacing before the closing line.
- **Sample Output:**
  ```
  -------- RECEIPT --------
  Item		Price
  Notebook	$2.50
  Pen		$1.00
  Eraser		$0.50
  --------------------------
  Total		$4.00

  Thank you for shopping!
  ```

## calculator.py (optional)
- **Aim:** Menu-driven calculator supporting add, subtract, multiply, divide, and exit, looping until the user chooses to exit.
- **Logic:** Wrap the menu in a `while True` loop; read the user's choice, validate it, then read two numbers and run the matching operation. `break` on exit, `continue` on invalid input, and guard division by zero.
- **Sample Input:** `1`, `5`, `3` (add 5 and 3), then `5` to exit
- **Sample Output:**
  ```
  Result: 8.0
  Goodbye!
  ```
