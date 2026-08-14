# greeting.py
# Takes a user's name, age, and city as input and prints
# one combined sentence using an f-string.

name = input("Enter your name: ")
age = input("Enter your age: ")   # kept as string, only used for display here
city = input("Enter your city: ")

# f-string lets us drop variables directly into the text using {}
print(f"Hi {name}, you are {age} years old and you live in {city}.")
