slope_degrees = 18.5       # degrees
rock_density = 3.2         # rocks per square meter
battery_level = 45         # percent


if slope_degrees < 15 and rock_density < 2:
    classification = "halt Or reroute"
elif slope_degrees < 20 and rock_density < 5:
    classification = "proceed with caution"
else:
    classification = "safe to  traverse"

                  

print(f"Terrain classification: {classification}")