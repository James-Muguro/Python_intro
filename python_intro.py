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


# Game
import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
num_guesses = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while True:
    guess = int(input("Enter your guess: "))
    num_guesses += 1

    if guess == secret_number:
        print(f"Congratulations, you guessed the number {secret_number} in {num_guesses} guesses!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
