# Define the range of numbers for the multiplication table
numbers = range(1, 11)

# Use a for loop to iterate through the numbers in the range
for number in numbers:
    # Use another for loop inside the main for loop to generate the multiplication table for each number
    for i in range(1, 11):
        # Use the continue statement to skip over even numbers
        if i % 2 == 0:
            continue
        # Print the multiplication table for each number
        print(number, 'x', i, '=', number*i)
    # Print a blank line after each multiplication table
    print()
