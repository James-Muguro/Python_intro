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


# Selling Tickets
# Create an empty list to store ticket information
tickets = []

while True:
    print("\n1. Sell Ticket")
    print("2. Print All Tickets")
    print("3. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the customer's name: ")
        num_tickets = int(input("Enter the number of tickets: "))

        # Create a dictionary to represent the ticket and add it to the list
        ticket = {"name": name, "num_tickets": num_tickets}
        tickets.append(ticket)

        print(f"\nSold {num_tickets} tickets to {name}!")
    elif choice == 2:
        print("\nAll Tickets:")
        for ticket in tickets:
            print(f"{ticket['name']} - {ticket['num_tickets']} tickets")
    elif choice == 3:
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")


# Lottery Game
import random

# Generate a list of 6 random numbers between 1 and 49
lottery_numbers = random.sample(range(1, 50), 6)

# Prompt the user to enter 6 numbers between 1 and 49
print("Welcome to the lottery! Please enter 6 numbers between 1 and 49.")
user_numbers = []

for i in range(6):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))

            # Check if the entered number is within the valid range (1 to 49)
            if num < 1 or num > 49:
                raise ValueError("Number must be between 1 and 49.")
            # Check if the entered number has already been chosen
            elif num in user_numbers:
                raise ValueError("Number already entered.")
            break
        except ValueError as e:
            print(e)
    user_numbers.append(num)

# Sort the user's numbers and the lottery numbers
user_numbers.sort()
lottery_numbers.sort()

# Print the user's numbers and the lottery numbers
print(f"\nYour numbers: {user_numbers}")
print(f"Lottery numbers: {lottery_numbers}")

# Check how many numbers match
matches = set(user_numbers).intersection(set(lottery_numbers))
num_matches = len(matches)

# Print the result
if num_matches == 6:
    print("\nCongratulations! You have won the jackpot!")
elif num_matches >= 3:
    print(f"\nYou have matched {num_matches} numbers and won a prize!")
else:
    print("\nHard Luck, you did not match any numbers. Please try again.")


# Creating Reservations
# Create a dictionary to represent the availability of tables
tables = {
    "Table 1": False,
    "Table 2": False,
    "Table 3": False,
    "Table 4": False,
    "Table 5": False
}

while True:
    # Display the available tables
    print("Available tables:")
    for table, available in tables.items():
        if not available:
            print(table)
    print()

    # Prompt the user to choose a table or quit
    table_choice = input("Choose a table (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if table_choice.lower() == "q":
        break

    # Check if the chosen table is valid
    if table_choice not in tables:
        print("Invalid choice.")
        continue

    # Check if the chosen table is available
    if tables[table_choice]:
        print("Sorry, that table is not available.")
        continue

    # Reserve the chosen table
    tables[table_choice] = True
    print("Table", table_choice, "has been reserved.")


# Aptitude Test
# Define the questions and answers as a dictionary
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest country in the world by land area?": "Russia",
    "What is the currency of Japan?": "Yen",
    "Who is the president of Kenya?": "William Ruto",
    "When did Covid-19 begin?": "January 2020",
    "Which is the largest ocean?": "Pacific",
    "How many countries does Africa have?": "Fifty four",
    "Kenyan staple food is?": "Ugali",
    "Is lesbianism legal in Kenya?": "No",
    "Which is the biggest company in East Africa": "Safaricom"
}

# Initialize a variable to keep track of the score
score = 0

# Ask the questions and evaluate answers
for question, answer in questions.items():
    print(question)
    user_answer = input("Your answer: ")

    # Check if the user's answer matches the correct answer (case-insensitive)
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", answer)
    print()

# Display the final score
print("Your score is", score, "out of", len(questions))


# Truth or Dare Game
import random

# Define the truth and dare prompts as lists
truth_prompts = [
    "What is your biggest fear?",
    "Have you ever lied to your best friend?",
    "What was the last thing you searched for on your phone?",
    "What is something you're embarrassed to admit you like?"
]

dare_prompts = [
    "Call your crush and confess your love to them (or a random number if you're single)",
    "Do 20 jumping jacks",
    "Send a funny meme to your entire contact list",
    "Sing a song in front of everyone"
]

# Randomly select a truth or dare prompt
is_truth = random.choice([True, False])
prompt = random.choice(truth_prompts if is_truth else dare_prompts)

# Prompt the user to answer the truth or complete the dare
if is_truth:
    print("Truth:", prompt)
    answer = input("Your answer: ")
    print("Thanks for being honest!")
else:
    print("Dare:", prompt)
    input("Press enter when you're ready...")
    print("Okay, here we go!")
    # Implement the dare here, e.g., you can print a message for the dare

print("Thanks for playing!")


# Days Countdown
import datetime

# Specify the target date
target_date = datetime.date(2023, 10, 31)

# Get today's date
today = datetime.date.today()

# Calculate the number of days until the target date
days_remaining = (target_date - today).days

# Print the countdown message
print(f"Only {days_remaining} day(s) left until {target_date.strftime('%B %d, %Y')}! Adios, guys. It's been real.")


# Young's Modulus
import numpy as np

# Input data
stress = np.array([100, 200, 300, 500, 700, 800, 1000, 1200, 1500, 1800])   # Stress in MPa
strain = np.array([0.001, 0.002, 0.003, 0.005, 0.007, 0.008, 0.01, 0.012, 0.015, 0.018])   # Strain

# Calculate Young's modulus
E = stress / strain

# Print the result
print(f"Young's modulus = {E.mean()} MPa")
