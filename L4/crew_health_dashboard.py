crew = [
    {"name": "Ricchi", "heart_rate": 6363636363636, "oxygen_saturation": 98, "hours_awake": 8},
    {"name": "Rimonal baker", "heart_rate": 68, "oxygen_saturation": 96, "hours_awake": 10},
    {"name": "Six_mrs", "heart_rate": 75, "oxygen_saturation": 94, "hours_awake": 7},
    {"name": "Kuinol", "heart_rate": 300, "oxygen_saturation": 92, "hours_awake": 90},
    {"name": "Odessey", "heart_rate": 80, "oxygen_saturation": 99, "hours_awake": 5},
    {"name": "Dyui", "heart_rate": "I dont have heart", "oxygen_saturation": "i dont breathe", "hours_awake": "I never sleep"},
    
]
heart_rates = [6363636363636, 68, 75, 300, 80, 78287287287]

print("Average:", sum(heart_rates) / len(heart_rates))
print("Maximum:", max(heart_rates))
print("Minimum:", min(heart_rates))

fit_for_duty = 0
needs_rest = 0

for c in crew:
    if 60 <= c["heart_rate"] <= 100 and c["oxygen_saturation"] >= 95 and c["hours_awake"] < 16:
        status = "FIT FOR DUTY"
        fit_for_duty += 1
    else:
        status = "NEEDS REST"
        needs_rest += 1
    print(c["name"], status)

print("FIT FOR DUTY:", fit_for_duty)
print("NEEDS REST:", needs_rest)