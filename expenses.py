#====================================
#  TRIPWISE - EXPENSES CALCULATIONS
#====================================

import pricing
import trip

#=====================================
# TECHNICAL FUNCTIONS
#=====================================

# Reject negative values for expenses
def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Amount cannot be negative. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#=====================================
# FUNCTIONS
#=====================================

# Show suggested daily budget, let the use adjust it, and return the final daily budget
def customize_daily_budget() :
    print(f"\nSuggested {label} budget : RM {suggested:,.2f} per person per day")
    options = [
        "Accepted suggested budget",
        "Increase budget by a percentage",
        "Decrease budget by a percentage",
        "Enter a custom budget amount"
    ]
    choice = trip.choose_from_list(f"Customize {label} budget : ", options)

    if choice == options[0]:
        return suggested

    if choice == options[1]:
        percent = trip.get_positive_float("Increase by (%) : ")
        return suggested * (1 + percent / 100)

    if choice == options[2]:
        while True:
            percent = trip.get_positive_float("Decrease by (%) : ")
            if 0 <= percent <= 100:
                return suggested * (1 - percent / 100)
            print("Decrease percentage must be between 0 and 100.")

    return get_non_negative_float("Enter custom budget amount (RM) : ")

# Calculate the accommodation, public transport, and return transport total for all travelers
def calculate_regional_costs(trip_info):
    prices = pricing.get_region_prices(trip_info["region"])
    season_multiplier = pricing.SEASON_MULTIPLIERS[trip_info["season"]]
    travelers = trip_info["travelers"]

    # Calculate costs

    # AC = A * H * N
    # Accommodation = Price per night * Number of nights * Number of travelers
    accommodation = prices["accommodation"] * trip_info["nights"] * travelers

    # PT = P * D * N
    # Public Transport = Price per day * Number of days * Number of travelers
    public_transport = prices["public_transport"] * trip_info["days"] * travelers

    # RT = B * R * S * N
    # Return Transport = Base price * Regional multiplier * Season multiplier * Number of travelers
    return_transport = prices["return_transport"] * season_multiplier * travelers

    return {
        "accommodation": accommodation,
        "public_transport": public_transport,
        "return_transport": return_transport
    }

