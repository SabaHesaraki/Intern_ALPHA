# trip.py
destination = "isfahan"
distance = 440  
consumption = 7.5  
fuel_price = 3000  
passengers = 3

total_fuel_used = (distance / 100) * consumption
total_cost = total_fuel_used * fuel_price
per_person_cost = total_cost / passengers

print("-" * 40)
print(f"Destination : {destination.strip().title()}")
print(f"Distance (km): {distance}")
print(f"Consumption (L/100km): {consumption}")
print(f"Fuel price: {fuel_price}")
print(f"Passengers: {passengers}")
print("-" * 40)
print(f"Trip to {destination.strip().title()}")
print(f"Fuel used     : {total_fuel_used:.1f} L")
print(f"Total cost    : {total_cost:,.0f}")
print(f"Per person    : {per_person_cost:,.0f}")
print(f"Distance      : {distance * 0.621371:.2f} mi")
print("-" * 40)

