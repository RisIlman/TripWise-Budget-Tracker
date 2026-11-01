# =========================================
# TRIPWISE
# Travel Budget Estimator & Itinerary Planner
# =========================================

import pricing

def main_menu () :
    print ("=========================================")
    print ("                 TRIPWISE                ")
    print ("=========================================")

    print("1. Plan New Trip")
    print("2. View Pricing Information")
    print("3. Exit")

    while True:
        choice = input("\nSelect an option : ")

        if choice == "1":
            print("Starting new trip planning...")
            # Here call the function to start planning a new trip
            break

        elif choice == "2":
            print("Displaying Pricing Information...")
            break

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please select a valid option.")


main_menu()