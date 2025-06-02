#Paul Fralix, 06/01/2025, Assignment 1.3
# Beer Bottles Countdown Program
# This program counts down the number of beer bottles on the wall, simulating the classic song "99 Bottles of Beer".    

#
def countdown(bottles): # Function to count down the number of bottles
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.") # Print current number of bottles
            print(f"Take one down and pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n") # Print next number of bottles
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.") # Print singular case for one bottle
            print("Take one down and pass it around, no more bottles of beer on the wall.\n") # Print case for no bottles left
        bottles -= 1

# Main Program
def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? ")) # User input for number of bottles
        # Validate input    
        if bottles < 1:
            print("Please enter a positive number greater than 0.") #   Error message for invalid input
            return
        countdown(bottles)
        print("Time to buy more beer!") # Final message after countdown
    except ValueError:
        print("Invalid input. Please enter a valid number.") # Error message for non-integer input

# Run the program
main()
