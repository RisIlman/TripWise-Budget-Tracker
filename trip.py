#====================================
# TRIPWISE - TRIP INFORMATION
#====================================

import pricing

#====================================
# TECHNICAL FUNCTIONS
#====================================

# Keep asking until the user enters a whole number >= minimum.
def get_positive_int(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Please enter a number that is at least {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
 
# Keep asking until the user enters a number greater than 0.
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter an amount greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
