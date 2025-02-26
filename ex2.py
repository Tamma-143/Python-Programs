# Variable assignments
name = "Subhu"
age = 25
height = 5.6
city = "Poduru"
favorite_color = "blue"
def greet(user_name):
    return f"Hello, {user_name}! Welcome to the Python world."
print(greet(name))
for i in range(1, 2):
    print(f"Number: {i}")
def calculate_square(number):
    return number * number
for number in range(1, 6):
    square = calculate_square(number)
    print(f"The square of {number} is {square}")

if age > 18:
    status = "adult"
else:
    status = "minor"

print(f"{name} is an {status}.")

# List of hobbies
hobbies = ["reading", "painting", "hiking"]
number_of_hobbies = len(hobbies)

# Function to print hobbies
def print_hobbies(hobby_list):
    for hobby in hobby_list:
        print(f"One of my hobbies is {hobby}")

# Print the hobbies
print_hobbies(hobbies)

# Additional conditional and loop
for i in range(5):
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")

# Dictionary to store user information
user_info = {
    "firstname": "Subhu",
    "lastname": "Doe",
    "age": 25,
    "city": "Poduru"
}

# Accessing dictionary values
print(f"Name: {user_info['firstname']} {user_info['lastname']}")
print(f"Age: {user_info['age']}")
print(f"City: {user_info['city']}")

# Adding a new key-value pair to the dictionary
user_info["favorite_color"] = favorite_color
print(f"Favorite Color: {user_info['favorite_color']}")

# List comprehension to generate squares of numbers 1 to 10
squares = [calculate_square(num) for num in range(1, 11)]
print(f"Squares of numbers from 1 to 10: {squares}")

# While loop
counter = 0
while counter < 5:
    print(f"Counter is at {counter}")
    counter += 1

# Final print statement
print("Script execution completed.")
