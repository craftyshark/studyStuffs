import csv
import random

# Define the number of records
num_records = 1000

# Open a new CSV file in write mode
with open('simulator_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Timestamp", "Tank Level", "Pump Status"])
    
    # Initialize tank level and pump status
    tank_level = 50.0
    pump_status = 0  # 0 for off, 1 for on
    
    # Generate records
    for i in range(num_records):
        # Update tank level and pump status
        if pump_status == 0 and tank_level <= 50:
            pump_status = 1
        elif pump_status == 1 and tank_level >= 100:
            pump_status = 0

        if pump_status == 0:
            tank_level -= random.uniform(0.1, 0.5)  # level decreases
        else:
            tank_level += random.uniform(0.1, 0.5)  # level increases

        # Ensure tank level stays within realistic bounds
        tank_level = max(0, min(100, tank_level))
        
        # Write the record
        writer.writerow([i, round(tank_level, 2), pump_status])
