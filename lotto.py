import random

# Create an empty list that will be used to store the lotto numbers!
lottery_numbers = []

for i in range(0, 6):
# "i" is a temporary variable used to store the integer value of the current position in the range of the for loop that only has scope within its for loop.
    lottery_number = random.randint(1, 50)
    # Check for previously selected numbers (if applicable) ...
    while lottery_number in lottery_numbers:
        # randomise numbers to prevent previously selected numbers being selected
        lottery_number = random.randint(1, 50)

    # Append the unique number to our created list.
    lottery_numbers.append(lottery_number)

# Sort the list in ascending order
lottery_numbers.sort()

# Print the list output on screen:
print(">>> Today's winning numbers are: ")
print(lottery_numbers)

