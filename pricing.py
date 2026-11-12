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
        "accommodation" : 1.525,
        "public_transport" : 1.280,
        "return_transport" : 11.27
    },

    "West Europe" : {
            "accommodation" : 1.725,
            "public_transport" : 1.140,
            "return_transport" : 10.96
        },

    "East Europe" : {
            "accommodation" : 0.950,
            "public_transport" : 0.360,
            "return_transport" : 11.02
        },

    "South Europe" : {
            "accommodation" : 1.400,
            "public_transport" : 0.640,
            "return_transport" : 11.12
        },

    "North Asia" : {
            "accommodation" : 0.700,
            "public_transport" : 0.300,
            "return_transport" : 4.90
        },

    "Central Asia" : {
            "accommodation" : 0.500,
            "public_transport" : 0.080,
            "return_transport" : 10.67
        },

    "Middle East" : {
            "accommodation" : 0.950,
            "public_transport" : 0.380,
            "return_transport" : 8.68
        },

    "ASEAN" : {
            "accommodation" : 1.0,
            "public_transport" : 1.0,
            "return_transport" : 1.0
        },

    "North America" : {
            "accommodation" : 1.750,
            "public_transport" : 0.560,
            "return_transport" : 16.13
        },

    "South America" : {
            "accommodation" : 0.725,
            "public_transport" : 0.280,
            "return_transport" : 26.23
        },

    "North Africa" : {
        "accommodation" : 0.850,
        "public_transport" : 0.120,
        "return_transport" : 12.19
    },

    "Oceania" : {
        "accommodation" : 1.550,
        "public_transport" : 0.720,
        "return_transport" : 9.20
    }
}

#==============================================
# ASEAN COUNTRY PRICES (MYR per person)
#==============================================

ASEAN_PRICING = {

    "Brunei" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Cambodia" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Indonesia" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Laos" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Myanmar" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Philippines" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Singapore" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Thailand" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    },

    "Vietnam" : {
        "accommodation" : 1,
        "public_transport" : 1,
        "return_transport" : 1
    }
}

ASEAN_COUNTRIES = list(ASEAN_PRICING.keys())

#==============================================
# SEASONAL MULTIPLIERS CONSTANTS
#==============================================

SEASON_MULTIPLIERS = {

    "Low" : 0.85,
    "Normal" : 1.00,
    "Peak" : 1.40
}

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

# Region names for the menu
def get_region_names():
    return["ASEAN"] + list(REGIONAL_PRICING.keys())

# Function to calculate the final regional prices based on the base prices and multipliers
def get_region_prices(region, country=None):
    if region == "ASEAN":
        multipliers = ASEAN_PRICING[country]
    else:
        multipliers = REGIONAL_PRICING[region]

    return {
        "accommodation": BASE_ACCOMMODATION * multipliers["accommodation"],
        "public_transport": BASE_PUBLIC_TRANSPORT * multipliers["public_transport"],
        "return_transport": BASE_RETURN_TRANSPORT * multipliers["return_transport"]
    }

def print_price_header(first_column):
    print(f"{first_column:<15}{'Accommodation':>15}{'Public Transport':>18}{'Return Transport':>18}")
    print(f"{'':<15}{'(per night)':>15}{'(per day)'}{'(per trip)':>18}")
    print("-" * 66)

def print_price_row(name, prices):
    print(f"{name:<15}"
          f"{'RM' + format(prices['accommodation'], ',.2f'):>15}"
          f"{'RM' + format(prices['public_transport'], ',.2f'):>15}"
          f"{'RM' + format(prices['return_transport'], ',.2f'):>15}")

# Function to display the pricing information in a formatted table
def display_pricing_information():
    print("\n================ PRICING INFORMATION ================")
    print("All prices are ESTIMATES in RM.")
    print("Return transport shown is normal season, per person.\n")

    print_price_header("Region")
    for region in REGIONAL_PRICING:
        print_price_row(region, get_region_prices(region))
    print("ASEAN          (price depends on the country, see below)")

    print("\nASEAN countries")
    print_price_header("Country")
    for country in ASEAN_PRICING:
        print_price_row(country, get_region_prices("ASEAN, country"))
 
    print("\nSeason multipliers (applied to return transport):")
    for season, multiplier in SEASON_MULTIPLIERS.items():
        print(f"  {season:<8}x{multiplier:.2f}")