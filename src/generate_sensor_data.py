
import csv
import random
from datetime import datetime, timedelta

filename = "data/sensor_data.csv"
start_time = datetime.now()

with open(filename, mode="w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "temperature_C",
        "voltage_V",
        "current_A"
    ])

    # Generate 20 sensor measurements
    for i in range(20):

        timestamp = start_time + timedelta(seconds=i)

        # Normal operating conditions
        temperature = round(random.uniform(40, 60), 2)
        voltage = round(random.uniform(225, 235), 2)
        current = round(random.uniform(4, 6), 2)

        # Inject abnormal operating conditions
        if i == 5:
            temperature = round(random.uniform(80, 95), 2)

        elif i == 10:
            voltage = round(random.uniform(190, 200), 2)

        elif i == 15:
            current = round(random.uniform(8.5, 10), 2)

        elif i == 18:
            voltage = round(random.uniform(255, 265), 2)

        writer.writerow([
            timestamp.isoformat(timespec="seconds"),
            temperature,
            voltage,
            current
        ])

print("Sensor dataset generated successfully!")
print("Total measurements: 20")
print("Simulated abnormal measurements: 4")
print("CSV file saved to:", filename)
