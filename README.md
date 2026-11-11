# TripWise

**Travel Budget Estimator & Itinerary Planner for Malaysian travelers**

TripWise is a terminal-based Python application that helps travelers departing from Malaysia estimate the cost of an overseas trip and organize their activities into a daily itinerary. It then compares the estimated total against the user's available budget.

> Course project: CSF21803 Software Development Fundamental, Semester I 2026/2027.

---

## Features

- **Budget estimator**: calculates accommodation, public transport and return transport from regional pricing multipliers, with a seasonal adjustment for return transport.
- **Customizable expenses**: suggested daily budgets for meals and miscellaneous spending. The user can accept, increase, decrease or replace them.
- **Itinerary planner**: the user enters their own attractions (name, price, area, preferred time slot) and the system schedules them across days and time slots, grouping attractions in the same area. The user can view, add, remove and move attractions.
- **Budget analysis**: totals every expense, shows the cost per person and reports whether the trip is *within budget*, *at the budget limit* or *exceeding budget*.
- **Input validation**: invalid input is rejected with a message instead of crashing the program.

## Scope

- Trips start and end at **Kuala Lumpur International Airport (KUL)**.
- Destinations are **overseas only**. Malaysia is not accepted as a destination.
- All prices are in **Malaysian Ringgit (RM)**.
- All results are **estimates**, not guaranteed prices.

---

## Requirements

- Python 3.8 or newer
- No external libraries (standard library only)

## How to run

1. Download or clone the project folder.
2. Open a terminal in the project folder.
3. Run:

```
python main.py
```

On some systems, use `python3 main.py` instead.

---

## How to use

1. From the main menu, choose **1. Plan New Trip**.
2. Enter the trip details: destination region, country, number of days, number of travelers, available budget (RM) and travel season.
3. Review the suggested meals and miscellaneous budgets, and accept or change each one.
4. Enter your attractions (or skip), review the generated itinerary and edit it if needed.
5. Read the trip summary: total estimated cost, cost per person, budget status and the final itinerary.

Choose **2. View Pricing Information** to see the calculated price per region, and **3. Exit** to quit.

### Example

Trip: Singapore (ASEAN), 5 days, 2 travelers, Normal season, suggested meals and miscellaneous budgets accepted, no attractions.

| Expense | Amount |
|---|---|
| Accommodation | RM960.00 |
| Public transport | RM150.00 |
| Return transport | RM1,062.00 |
| Meals | RM600.00 |
| Miscellaneous | RM300.00 |
| **Total** | **RM3,072.00** |

---

## Project structure

```
TripWise/
├── main.py        # Main menu and program flow
├── pricing.py     # Base prices, regional and seasonal multipliers, suggestions
├── trip.py        # Trip information input and input validation helpers
├── expenses.py    # Expense calculations and meals/miscellaneous customization
├── itinerary.py   # Attraction input, scheduling and itinerary editing
├── summary.py     # Final budget calculation, budget analysis and trip summary
└── README.md
```

| Module | Responsibility |
|---|---|
| `main.py` | Shows the menu and calls the other modules in order |
| `pricing.py` | Stores all pricing constants and shows the pricing table |
| `trip.py` | Collects destination, duration, travelers, budget and season |
| `expenses.py` | Calculates regional costs and the preliminary budget |
| `itinerary.py` | Schedules attractions and calculates the attraction total |
| `summary.py` | Combines all costs, compares with the budget and prints the summary |

---

## How the budget is calculated

Base prices (RM): accommodation 200 per person per night, public transport 50 per person per day, return transport 300 per person per round trip.

Each region has a multiplier for each of the three categories:

```
Estimated price = Base price x Regional multiplier
```

| Expense | Formula |
|---|---|
| Accommodation | price x nights x travelers |
| Public transport | price x days x travelers |
| Return transport | base x regional multiplier x seasonal multiplier x travelers |
| Meals | daily budget x days x travelers |
| Miscellaneous | daily budget x days x travelers |
| Attractions | sum of scheduled attraction prices x travelers |

```
Total budget     = accommodation + public transport + return transport
                   + meals + miscellaneous + attractions
Cost per person  = total budget / travelers
Remaining budget = available budget - total budget
```

Seasonal multipliers (return transport only): Low 0.85, Normal 1.00, Peak 1.40.

### Regions

ASEAN, North Asia, Central Asia, Middle East, North Europe, West Europe, South Europe, East Europe, North Africa, North America, South America, Oceania.

All ASEAN countries (except Malaysia) share one ASEAN multiplier.

---

## Testing

The application was tested with valid, boundary and invalid inputs, including:

- a trip within budget, exceeding budget and exactly at the budget limit
- invalid inputs (Malaysia as destination, non-numeric or too-small values, negative budget)
- a trip with no attractions
- more attractions than available time slots
- different regions, seasons and group sizes

See the project report for the full test-case table.

---

## Limitations

- Prices are **estimates** based on regional multipliers, not live prices.
- Several multipliers and expense suggestions are **placeholder values** pending pricing research. Only the ASEAN return-transport multiplier (1.77) is based on researched fares. Update the numbers in `pricing.py`; no other code needs to change.
- No city-level price differences. Seasonal multipliers are global, not per region.
- Costs are calculated per person and multiplied by the number of travelers. Shared costs (for example, a room split between two people) are not modelled.
- Attractions that do not fit in the schedule are flagged as unscheduled and **excluded** from the cost.
- Trips are not saved. Data is lost when the program exits.

## Future development

- Replace placeholder multipliers with researched, regularly updated pricing data
- Regional seasonal multipliers and automatic season detection from travel dates
- Saving and loading trips
- Shared-cost handling
- Web or mobile interface, live flight and attraction prices, multi-currency support

---

## Team

| Name | Role |
|---|---|
| _Member 1_ | _e.g. Programming_ |
| _Member 2_ | _e.g. Programming_ |
| _Member 3_ | _e.g. Pricing research_ |
| _Member 4_ | _e.g. Pricing research_ |
| _Member 5_ | _e.g. Report and presentation_ |