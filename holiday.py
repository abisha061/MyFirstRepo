# Issue 1: Make Method Parameters Descriptive: Instead of using generic names like 'city_flight', 'num_nights' and 'num_days', use more descriptive names.
def plane_cost(city_flight):
    # Calculate plane cost based on the chosen city
    if city_flight == "New York":
        return 500 # Replace with actual cost for New York    
    elif city_flight == "Los Angeles":
        return 450 # Replace with actual cost for Los Angeles
    # Add more cities as needed
    else:
        return 0  # Default value if city is not recognized
# Issue 2: Use constants for Daily Rental Cost and Nightly cost: use constants for the daily rental cost and nightly cost instead of hardcoding them in functions.
def car_rental_cost(num_days):
    # Calculate car rental cost based on the number of days
    daily_rental_cost = 50  # Replace with actual daily rental cost
    return num_days * daily_rental_cost
# Issue 3: Add comments for Clarity: Add comments to explain the purpose of each function and any complex logic.
def hotel_cost(num_nights):
    # Calculate hotel cost based on the number of nights
   nightly_cost = 100  # Replace with actual nightly cost
   return num_nights * nightly_cost

# Issue 4: Handle Case-Insensitive City Comparison: Make the comparison of the chosen city case-sensitive.
def holiday_cost(hotel_cost, plane_cost, car_rental_cost):
    # Calculate the total holiday cost
    total_cost = hotel_cost + plane_cost + car_rental_cost
    return total_cost
# Issue 5: Improve Printing: Print the total cost with proper formatting
def print_details(city_flight, num_nights, num_days):
    # Print out the details of the holiday
    print("Holiday Details:")
    print("Destination City:", city_flight)
    print("Number of Nights in Hotel:", num_nights)
    print("Number of Days for Car Rental:", num_days)

# Get user inputs
city_flight = input("Enter the city they will be flying to: ")
num_nights = int(input("Enter the number of nights they will be staying at a hotel: "))
num_days = int(input("Enter the number of days they will be renting a car: "))

# Calculate individual costs
hotel_cost = hotel_cost(num_nights)
plane_cost = plane_cost(city_flight)
car_rental_cost = car_rental_cost(num_days)

# Calculate total cost
total_cost = holiday_cost(hotel_cost, plane_cost, car_rental_cost)

# Print details
print_details(city_flight, num_nights, num_days)

# Print the total cost
print("Total holiday cost: $", total_cost)
