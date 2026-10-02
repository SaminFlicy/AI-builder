import random
import math

def check_ship(ship_name):
    fuel = random.randint(0, 100)
    health = random.randint(0, 100)
    return fuel, health

def overall_status(fuel, health):
    if fuel >= 60 and health >= 60:
        return "READY"
    elif fuel < 30 or health < 30:
        return "GROUNDED"
    else:
        return "NEEDS ATTENTION"

ships = ["Savager", "Dyui", "Getleer", "Six_seven", "Odessey"]

ready = 0
grounded = 0
fuel_total = 0

for ship in ships:
    fuel, health = check_ship(ship)
    status = overall_status(fuel, health)
    print(ship, fuel, health, status)

    

   

print("READY:", ready)
print("GROUNDED:", grounded)
print("Average fuel:", math.floor(fuel_total / len(ships)))


