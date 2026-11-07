#=================================
# TRIPWISE - ITINERARY PLANNER
#=================================

import expenses
import trip

SLOTS = ["Morning", "Afternoon", "Evening"]
SLOT_TIMES = {
    "Morning"    : "9.00 AM",
    "Afternoon"  : "2.00 PM",
    "Evening"    : "5.00 PM"
}

#==================================
# TECHNICAL FUNCTIONS
#==================================

# Return True for yes, False for no
def ask_yes_no(prompt) :
    while True :
        answer = input(prompt + " (y/n) : ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")

#==================================
# FUNCTIONS
#==================================

# Ask the user to input attractions details
def get_attraction_details():
    print("\n--- Add Attraction ---")

    while True :
        name = input("Attraction Name : ").strip()
        if name != "" :
            break
        print("Name cannot be empty.")

    price = expenses.get_non_negative_float("Price (RM) per person (enter 0 if free) : ")

    area = input("Area / location (press Enter to skip) : ").strip().title()
    if area == "" :
        area = "Unspecified"

    slot = trip.choose_from_list("Preferred time slot : ", SLOTS)

    # day stays None until the attraction is displayed in the schedule
    return {
        "name"  : name,
        "price" : price,
        "area"  : area,
        "slot"  : slot,
        "day"   : None
    }

#===================================
# SCHEDULING FUNCTIONS
#===================================

# Check available slots
def slot_is_free(attractions, day, slot):
    for item in attractions :
        if item["day"] == day and item["slot"] == slot :
            return False
    return True

#Check if the day already contains an attraction in the same area
def day_has_area(attractions, day, area):
    if area == "Unspecified" :
        return False

    for item in attractions:
        if item["day"] == day and item["area"] == area:
            return True
    return False

# Place an attraction in the best free slot
def place_attraction(attractions, item, days):
    # Order preference :
    # 1. A day that has already the same area (preferred slot)
    # 2. A day that has already the same area (any free slot)
    # 3. The earliest day with the preferred slot free
    # 4. Any free slot
    # return True = placed , False = full schedule

    area = item["area"]

    # order 1 and 2 = the same area on the same day
    for day in range(1, days + 1):
        if day_has_area(attractions, day, area):
            if slot_is_free(attractions, day, item["slot"]):
                item["day"] = day
                return True

    for day in range(1, days + 1):
        if day_has_area(attractions, day, area):
            for slot in SLOTS :
                if slot_is_free(attractions, day, area):
                    item["day"] = day
                    item["slot"] = slot
                    return True

    # order 3 = preferred slot on the earliest day
    for day in range(1, days + 1):
        if slot_is_free(attractions, day, item["slot"]):
            item["day"] = day
            item["slot"] = slot
            return True

    # order 4 = any free slot
    for day in range(1, days + 1):
        for slot in SLOTS :
            if slot_is_free(attractions, day, slot):
                item["day"] = day
                item["slot"] = slot
                return True

    item["day"] = None
    return False

# Sort key : group by area first then by time of day
def area_and_slot_order(item):
    return (item["slot"], SLOTS.index(item["slot"]))

# Automatic schedule all attractions.
# Same area attractions are placed next to each other and same day
def assign_to_days(attractions, days):
    for item in attractions :
        item["day"] = None

    for item in sorted(attractions, key=area_and_slot_order) :
        place_attraction(attractions, item, days)

#=====================================
# DISPLAY FUNCTIONS
#=====================================

# Calculate total cost attractions for all travelers
def calculate_attraction_total(attractions, travelers):
    per_person = 0

    for item in attractions:
        if ["item"] is not None :
            per_person += item["price"]
        return per_person * travelers

# Print total day-by-day schedule, unscheduled attractions and total
def display_itinerary(attractions, days, travelers):
    print("\n================ ITINERARY ================")

    for day in range(1, days + 1):
        print(f"\nDay {day}")
        for slot in SLOTS :
            line = f"   {SLOT_TIMES[slot]:>8}   {slot:<10}"
            found = False
            
            for item in attractions:
                if item["day"] == day and item["slot"] == slot:
                    print(f"{line}{item['name']} ({item['area']}) RM {item['price']:,.2f} pp")
                    found = True
            if not found :
                print(f"{line}-- free --")

    unscheduled = [item for item in attractions if item["day"] is None]
    if unscheduled :
        print("\n!! UNSCHEDULED (no free slot, NOT included in the cost)!!")
        for item in unscheduled :
            print(f"  - {item['name']} ({item['area']}) RM {item['price']:,.2f} pp")

    total = calculate_attraction_total(attractions, travelers)
    print("\n" + "-" * 43)
    print(f"Total attraction expenses ({travelers} traveler(s)) : RM{total:,.2f}")

#===============================
# EDITING FUNCTIONS
#===============================

# One line label for menus
def describe(item):
    if item["day"] is None :
        place = "unscheduled"
    else :
        place = f"Day {item['day']} {item['slot']}"
    return f"{item['name']} - {place}"

# Remove attraction from list
def remove_attraction(attractions):
    if not attractions:
        print("There are no attractions to remove.")
        return
    chosen = trip.choose_from_list("Remove which attraction ?", [describe(a) for a in attractions])
    attractions.pop([describe(a) for a in attractions].index(chosen))
    print("Attraction removed.")

# Rearrange attraction from list
def move_attraction(attractions, days):
    if not attractions :
        print("There are no attractions to move.")
        return

    labels = [describe(a) for a in attractions]
    item = attractions[labels.index(trip.choose_from_list("Move which attraction ? ", labels))]

    while True:
        day = trip.get_positive_int(f"Move to which day (1-{days}) : ")
        if day <= days:
            break
        print(f"Please enter a day between 1 and {days}")

    slot = trip.choose_from_list("Move to which time slot ? ", SLOTS)

    if slot_is_free(attractions, day, slot):
        item["day"] = day
        item["slot"] = slot
        print("Attraction moved.")
    else :
        print("That slot is already taken. Nothing was changed.")

# Add attraction to the list
def add_attraction(attractions, days):
    item = get_attraction_details()
    attractions.append(item)
    if place_attraction(attractions, item, days):
        print(f"Scheduled on Day {item['day']} ({item['slot']}).")
    else :
        print("No free slot left. The attraction is flagged as unscheduled.")

# Edit itinerary from the list
def edit_itinerary(attractions, days, travelers):
    options = [
        "View itinerary",
        "Add attraction",
        "Remove attraction",
        "Move attraction",
        "Finish"
    ]

    while True :
        choice = trip.choose_from_list("Itinerary options : ", options)

        if choice == "View itinerary":
            display_itinerary(attractions, days, travelers)
        elif choice == "Add attraction":
            add_attraction(attractions, days)
        elif choice == "Remove attraction":
            remove_attraction(attractions)
        elif choice == "Move attraction":
            move_attraction(attractions, days)
        else :
            break

#===============================
# PLAN ITINERARY FUNCTION
#===============================

def plan_itinerary(trip_info):
    days = trip_info["days"]
    travelers = trip_info["travelers"]
    attractions = []

    print("\n======== PLAN YOUR ITINERARY ========")
    print(f"Your trip das {days} day(s) with 3 time slots per day.")
    print("Enter the attractions you want to visit (optional).")

    while ask_yes_no("\nAdd an attraction ? "):
        attractions.append(get_attraction_details())

    assign_to_days(attractions, days)
    display_itinerary(attractions, days, travelers)

    if ask_yes_no("\nEdit the itinerary ? "):
        edit_itinerary(attractions, days, travelers)
        display_itinerary(attractions, days, travelers)

    return attractions, calculate_attraction_total(attractions, travelers)
