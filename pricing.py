#=================================================
# THIS IS TRIPWISE - PRICING CONFIGURATION FILE
#=================================================
# All pricing are in MYR (RM)

#==============================================
# GLOBAL BASE PRICES
#==============================================

BASE_ACCOMMODATION = 200           # per person per night
BASE_PUBLIC_TRANSPORT = 50         # per person per day
BASE_RETURN_TRANSPORT = 300        # per person for return trip

#==============================================
# REGIONAL MULTIPLIERS CONSTANTS
#==============================================

REGIONAL_PRICING = {

    "North Europe" : {
        "accommodation" : 15,
        "public_transport" : 10,
        "return_transport" : 11.67
    },

    "West Europe" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "East Europe" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "South Europe" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "North Asia" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 5.0
        },

    "Central Asia" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "Middle East" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "ASEAN" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "North America" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 13.33
        },

    "South America" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "North Africa" : {
        "accommodation" : 1.0,
        "public_transport" : 1.0,
        "return_transport" : 1.0
    },

    "Oceania" : {
        "accommodation" : 1.0,
        "public_transport" : 1.0,
        "return_transport" : 8.33
    }
}

#==============================================
# SEASONAL MULTIPLIERS CONSTANTS
#==============================================

SEASON_MULTIPLIERS = {

    "Low" : 0.85,
    "Normal" : 1.00,
    "Peak" : 1.40
}

#==============================================
# ASEAN COUNTRIES LIST (Malaysia excluded)
#==============================================
ASEAN_COUNTRIES = [
    "Brunei",
    "Cambodia",
    "Indonesia",
    "Laos",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam"
]

#==============================================
# SUGGESTED DAILY EXPENSES (per person / day)
# NEED TO BE ADJUSTED BASED ON REGION RESEARCH FURTHER
#==============================================
EXPENSE_SUGGESTION = {
    "ASEAN" :                 {"meals" : 60,   "miscellaneous" : 30},
    "North Asia" :            {"meals" : 100,  "miscellaneous" : 50},
    "Central Asia" :          {"meals" : 50,   "miscellaneous" : 30},
    "Middle East" :           {"meals" : 80,   "miscellaneous" : 40},
    "North Europe" :          {"meals" : 150,  "miscellaneous" : 70},
    "West Europe" :           {"meals" : 130,  "miscellaneous" : 60},
    "South Europe" :          {"meals" : 100,  "miscellaneous" : 50},
    "East Europe" :           {"meals" : 70,   "miscellaneous" : 35},
    "North Africa" :          {"meals" : 50,   "miscellaneous" : 30},
    "North America" :         {"meals" : 140,  "miscellaneous" : 70},
    "South America" :         {"meals" : 70,   "miscellaneous" : 40},
    "Oceania" :               {"meals" : 130,  "miscellaneous" : 60}
}


#==============================================
# FUNCTIONS
#==============================================

# Function to calculate the final regional prices based on the base prices and multipliers
def get_region_prices(region):
    multipliers = REGIONAL_PRICING[region]

    return {
        "accommodation": BASE_ACCOMMODATION * multipliers["accommodation"],
        "public_transport": BASE_PUBLIC_TRANSPORT * multipliers["public_transport"],
        "return_transport": BASE_RETURN_TRANSPORT * multipliers["return_transport"]
    }

# Function to display the pricing information in a formatted table
def display_pricing_information():
    print("\n================ PRICING INFORMATION ================")
    print("All prices are ESTIMATES in RM.")
    print("Return transport shown is normal season, per person.\n")
 
    print(f"{'Region':<15}{'Accommodation':>15}{'Public Transport':>18}{'Return Transport':>18}")
    print(f"{'':<15}{'(per night)':>15}{'(per day)':>18}{'(per trip)':>18}")
    print("-" * 66)
 
    for region in REGIONAL_PRICING:
        prices = get_region_prices(region)
        print(f"{region:<15}"
              f"{'RM' + format(prices['accommodation'], ',.2f'):>15}"
              f"{'RM' + format(prices['public_transport'], ',.2f'):>18}"
              f"{'RM' + format(prices['return_transport'], ',.2f'):>18}")
 
    print("\nSeason multipliers (applied to return transport):")
    for season, multiplier in SEASON_MULTIPLIERS.items():
        print(f"  {season:<8}x{multiplier:.2f}")