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

