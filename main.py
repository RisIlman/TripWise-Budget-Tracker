# =========================================
# TRIPWISE
# Travel Budget Estimator & Itinerary Planner
# =========================================

import pricing

def print_menu() :
    print("=========================================")
    print("                 TRIPWISE                ")
    print("=========================================")
    print("1. Plan New Trip")
    print("2. View Pricing Information")
    print("3. Exit")

def main() :
    while True:
        print_menu()
        choice = input("\nSelect an option : ").strip()

        if choice == "1":
            print("Starting new trip planning...")
            # call the trip.py later

        elif choice == "2":
            print("Displaying Pricing Information...")
            pricing.display_pricing_information()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


main()