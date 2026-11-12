#===========================================
# TRIPWISE - BUDGET ANALYSIS & TRIP SUMMARY
#===========================================

import itinerary

EXPENSE_LABELS = {
    "accommodation"    : "Accommodation",
    "public_transport" : "Public transport",
    "return_transport" : "Return transport",
    "meals"            : "Meals",
    "miscellaneous"    : "Miscellaneous",
    "attractions"      : "Attractions"
}

#========================
# FUNCTIONS
#========================

# Combine every expenses and compare against the available budget
def calculate_final_budget(costs, attraction_total, travelers, available_budget):
    breakdown = {
        "accommodation"      : costs["accommodation"],
        "public_transport"   : costs["public_transport"],
        "return_transport"   : costs["return_transport"],
        "meals"              : costs["meals"],
        "miscellaneous"      : costs["miscellaneous"],
        "attractions"        : attraction_total
    }

    # Total Breakdown = AC + PT + RT + MC + AT + EX
    total = round(sum(breakdown.values()), 2)
    remaining = round(available_budget - total, 2)

    breakdown_pp = {}
    for key, value in breakdown.items():
        breakdown_pp[key] = value / travelers

    return {
        "breakdown"    : breakdown,
        "breakdown_pp" : breakdown_pp,
        "total"        : total,
        "per_person"   : total / travelers,
        "budget_pp"    : available_budget / travelers,
        "remaining"    : remaining,
        "remaining_pp" : remaining / travelers,
        "status"       : get_budget_status(remaining)
    }

# Return budget status in text
def get_budget_status(remaining):
    if remaining > 0 :
        return "WITHIN BUDGET"
    if remaining < 0 :
        return "EXCEEDING BUDGET"
    return "AT BUDGET LIMIT"

def money(value, width=12):
    return "RM" + format(value, f">{width},.2f")

def print_money_row(label, total, per_person):
    print(f"{label:<20}{money(total)}   {money(per_person)}")

# Print complete budget itinerary
def display_trip_summary(trip_info, final, attractions):
    line = "-" * 51
 
    print("\n" + "=" * 51)
    print("             TRIPWISE TRIP SUMMARY")
    print("=" * 51)
    print(f"Destination : {trip_info['country']} ({trip_info['region']})")
    print(f"Duration    : {trip_info['days']} days / {trip_info['nights']} nights")
    print(f"Travelers   : {trip_info['travelers']}")
    print(f"Season      : {trip_info['season']}")
 
    print("\n--- ESTIMATED EXPENSES ---")
    print(f"{'':<20}{'Total':>14}   {'Per person':>14}")
    for key, label in EXPENSE_LABELS.items():
        print_money_row(label, final["breakdown"][key], final["breakdown_pp"][key])
    print(line)
    print_money_row("TOTAL ESTIMATED", final["total"], final["per_person"])
 
    print("\n--- BUDGET ANALYSIS ---")
    print(f"{'':<20}{'Total':>14}   {'Per person':>14}")
    print_money_row("Available budget", trip_info["budget"], final["budget_pp"])
 
    if final["remaining"] >= 0:
        print_money_row("Remaining", final["remaining"], final["remaining_pp"])
    else:
        print_money_row("Over budget by", -final["remaining"], -final["remaining_pp"])
    print(f"Status: {final['status']}")
 
    if final["status"] == "EXCEEDING BUDGET":
        biggest = max(final["breakdown"], key=final["breakdown"].get)
        print(f"Tip: your biggest expense is {EXPENSE_LABELS[biggest].lower()}. "
              "Reducing it would help most.")
 
    itinerary.display_itinerary(attractions, trip_info["days"], trip_info["travelers"])
 
    print("\nNote: all figures are estimates, not guaranteed prices.")