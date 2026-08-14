# string_manipulation.py
# Takes a full name as input and prints it in uppercase,
# lowercase, reversed, and prints its length.
# Uses three string methods: .strip(), .upper(), .lower()

full_name = input("Enter your full name: ").strip()  # strip() removes extra spaces

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())

# Reversing a string: slicing with a step of -1 walks backwards
# through the string from the last character to the first.
print("Reversed:", full_name[::-1])

print("Length:", len(full_name))
