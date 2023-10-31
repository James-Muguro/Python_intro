# This program prints "Hello World" to the console.

# Define a variable containing the string "Hello World"
message = "Hello World"

# Print the value of the 'message' variable to the console
print(message)


# This program demonstrates a for loop to print a list of surnames.

# Define a tuple containing surnames
surnames = ("Muthoni", "Karmago", "Njuguna", "Omondi", "Kibet", "Kigen", "Mutiso")

# Iterate through the surnames and print each one
for name in surnames:
    print(name)


# Random Numbers
import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(f"Random Integer: {random_number}")

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(f"Random Float: {random_float}")

# Generate a random element from a list
my_list = ['Windows', 'MacOS', 'Android']
random_element = random.choice(my_list)
print(f"Random Element from List: {random_element}")

# Shuffle the elements in a list
random.shuffle(my_list)
print(f"Shuffled List: {my_list}")


# Taking Inputs from Users
# Prompt the user for their name
name = input("What is your name?: ")

# Prompt the user for their age
age = input("How old are you?: ")

# Print a greeting with the user's name and age
print(f"Hello, my name is {name}, and I am {age} years old")
