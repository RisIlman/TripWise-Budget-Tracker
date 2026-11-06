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



#====================================
# FUNCTIONS
#====================================

# Show a numbered menu and return the user choice
def choose_from_list(title, options):
    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")
 
    while True:
        choice = get_positive_int("Select an option : ")
        if choice <= len(options):
            return options[choice - 1]
        print("Invalid choice. Please select a number from the list.")

# Ask user for destination country and return the country name (exclude Malaysia)
def get_destination_country(region) :
    if region == "ASEAN":
        print("ASEAN destinations: " + ", ".join(pricing.ASEAN_COUNTRIES))
 
    while True:
        country = input("Enter Destination Country : ").strip()
 
        if country == "":
            print("Country cannot be empty.")
        elif country.lower() == "malaysia":
            print("TripWise is for overseas trips only. Please choose a country outside Malaysia.")
        else:
            return country.title()

# Collect all trip details and return them as a dictionary
def get_trip_information():
    print("\n======== PLAN YOUR TRIP ========")
    print("Departure and return airport: KLIA (Kuala Lumpur International Airport)")
 
    region = choose_from_list("Select Destination Region : ", list(pricing.REGIONAL_PRICING.keys()))
    country = get_destination_country(region)
 
    days = get_positive_int("Number of travel days : ", minimum=2)
    travelers = get_positive_int("Number of travelers : ")
    available_budget = get_positive_float("Total available budget (RM) : ")
 
    season = choose_from_list("Select Travel Season : ", list(pricing.SEASON_MULTIPLIERS.keys()))
 
    return {
        "region": region,
        "country": country,
        "days": days,
        "nights": days - 1,
        "travelers": travelers,
        "budget": available_budget,
        "season": season
    }