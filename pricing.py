#==========================================
# THIS IS TRIPWISE - PRICING CONFIGURATION FILE
#==========================================

# GLOBAL BASE PRICES

BASE_ACCOMODATION = 200
BASE_PUBLIC_TRANSPORT = 50
BASE_RETURN_TRANSPORT = 300

# REGIONAL MULTIPLIERS CONSTANTS

REGIONAL_PRICING = {

    "ASEAN" : {
        "accommodation" : 5,
        "public_transport" : 3,
        "return_transport" : 1.77
    },

    "North Europe" : {
        "accommodation" : 15,
        "public_transport" : 10,
        "return_transport" : 11.67
    },

    "North Asia" : {
        "accommodation" : 8,
        "public_transport" : 5,
        "return_transport" : 5.00
    }
}



# SEASONAL MULTIPLIERS CONSTANTS

SEASON_MULTIPLIERS = {

    "Low" : 0.85,
    "Normal" : 1.00,
    "Peak" : 1.40
}