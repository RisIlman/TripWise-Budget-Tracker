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

