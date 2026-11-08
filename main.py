# =========================================
# TRIPWISE
# Travel Budget Estimator & Itinerary Planner
# =========================================

import pricing
import trip
import expenses
import itinerary
import summary

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

            attractions, attraction_total = itinerary.plan_itinerary(trip_info)

            final = summary.calculate_final_budget(
                costs, attraction_total,
                trip_info["travelers"], trip_info["budget"])
            summary.display_trip_summary(trip_info, final, attractions)

        elif choice == "2":
            pricing.display_pricing_information()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


main()