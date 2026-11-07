# =========================================
# TRIPWISE
# Travel Budget Estimator & Itinerary Planner
# =========================================

import pricing
import trip
import expenses

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
            trip_info = trip.get_trip_information()

            costs = expenses.calculate_preliminary_budget(trip_info)
            expenses.display_preliminary_budget(trip_info, costs)
            # Stage 3 will add the itinerary and attraction costs here

        elif choice == "2":
            pricing.display_pricing_information()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


main()