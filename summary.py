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

    return {
        "breakdown"   : breakdown,
        "total"       : total,
        "per_person"  : total / travelers,
        "remaining"   : remaining,
        "status"      : get_budget_status(remaining)
    }

# Return budget status in text
def get_budget_status(remaining):
    if remaining > 0 :
        return "WITHIN BUDGET"
    if remaining < 0 :
        return "EXCEEDING BUDGET"
    return "AT BUDGET LIMIT"

# Print complete budget itinerary
def display_trip_summary(trip_info, final, attractions):
    print("\n" + "=" * 55)
    print("               TRIPWISE TRIP SUMMARY")
    print("=" * 55)
    print(f"Destination : {trip_info['country']} ({trip_info['region']})")
    print(f"Duration    : {trip_info['days']} days / {trip_info['nights']} nights")
    print(f"Travelers  : {trip_info['travelers']}")
    print(f"Season      : {trip_info['season']}")
 
    print("\n--- ESTIMATED EXPENSES ---")
    for key, label in EXPENSE_LABELS.items():
        print(f"{label:<22}RM {final['breakdown'][key]:>12,.2f}")
    print("-" * 55)
    print(f"{'TOTAL ESTIMATED':<22}RM {final['total']:>12,.2f}")
    print(f"{'Cost per person':<22}RM {final['per_person']:>12,.2f}")
 
    print("\n--- BUDGET ANALYSIS ---")
    print(f"{'Available budget':<22}RM {trip_info['budget']:>12,.2f}")
 
    if final["remaining"] >= 0:
        print(f"{'Remaining':<22}RM {final['remaining']:>12,.2f}")
    else:
        print(f"{'Over budget by':<22}RM {-final['remaining']:>12,.2f}")
    print(f"Status: {final['status']}")
 
    if final["status"] == "EXCEEDING BUDGET":
        biggest = max(final["breakdown"], key=final["breakdown"].get)
        print(f"Tip: your biggest expense is {EXPENSE_LABELS[biggest].lower()}. "
              "Reducing it would help most.")
 
    itinerary.display_itinerary(attractions, trip_info["days"], trip_info["travelers"])
 
    print("\nNote: all figures are estimates, not guaranteed prices.")