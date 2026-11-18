
import csv
import math
from datetime import datetime
from pathlib import Path

filename = "data/sensor_data.csv"

# Read the CSV dataset
with open(filename, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    sensor_data = list(reader)

print("Industrial Sensor Data Analyzer")
print("--------------------------------")
print("Total measurements:", len(sensor_data))

# Check whether the dataset is empty
if not sensor_data:
    raise ValueError("The sensor dataset is empty.")

# Store validated measurements
validated_data = []

# Validate every measurement
for number, measurement in enumerate(sensor_data, start=1):

    try:
        timestamp = datetime.fromisoformat(measurement["timestamp"])
        temperature = float(measurement["temperature_C"])
        voltage = float(measurement["voltage_V"])
        current = float(measurement["current_A"])

    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(
            f"Invalid measurement {number}: {error}"
        ) from error

    # Reject NaN and infinity values
    if not all(math.isfinite(value) for value in
               [temperature, voltage, current]):
        raise ValueError(f"Non-finite value in measurement {number}")

    # Store the validated record
    validated_data.append({
        "timestamp": timestamp,
        "temperature_C": temperature,
        "voltage_V": voltage,
        "current_A": current
    })

print("\nData validation completed successfully!")
print("Valid measurements:", len(validated_data))
print("First validated measurement:", validated_data[0])


# Calculate sensor statistics
print("\nIndustrial Sensor Statistics")
print("----------------------------")

# Define the sensor parameters and their units
sensors = [
    ("temperature_C", "°C"),
    ("voltage_V", "V"),
    ("current_A", "A")
]

for sensor_name, unit in sensors:

    # Collect all measurements for the selected sensor
    values = []

    for measurement in validated_data:
        values.append(measurement[sensor_name])

    # Calculate statistics
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)

    # Display results
    print(f"\n{sensor_name}")
    print(f"Minimum: {minimum:.2f} {unit}")
    print(f"Maximum: {maximum:.2f} {unit}")
    print(f"Average: {average:.2f} {unit}")

# Detect abnormal operating conditions
print("\nIndustrial Sensor Fault Detection")
print("---------------------------------")

abnormal_count = 0
fault_records = []

# Check every validated measurement
for number, measurement in enumerate(validated_data, start=1):

    temperature = measurement["temperature_C"]
    voltage = measurement["voltage_V"]
    current = measurement["current_A"]
    timestamp = measurement["timestamp"]

    # Store detected faults for this measurement
    faults = []

    # Temperature threshold
    if temperature > 75:
        faults.append(f"OVERHEATING: {temperature:.2f} °C")

    # Voltage thresholds
    if voltage < 207:
        faults.append(f"UNDERVOLTAGE: {voltage:.2f} V")

    elif voltage > 253:
        faults.append(f"OVERVOLTAGE: {voltage:.2f} V")

    # Current threshold
    if current > 8:
        faults.append(f"OVERCURRENT: {current:.2f} A")

    # Display warnings if faults were detected
    
    if faults:
        abnormal_count += 1

        # Store the detected faults
        fault_records.append({
            "measurement_number": number,
            "timestamp": timestamp,
            "faults": faults
        })

        # Display warnings
        print(f"\nWARNING - Measurement {number}")
        print("Timestamp:", timestamp)

        for fault in faults:
            print(fault)


# Display fault detection summary
print("\nFault Detection Summary")
print("-----------------------")
print("Total measurements:", len(validated_data))
print("Abnormal measurements:", abnormal_count)
print("Normal measurements:", len(validated_data) - abnormal_count)
print("Stored fault records:", len(fault_records))


# Generate industrial sensor analysis report
print("\nGenerating Engineering Analysis Report...")

# Create reports directory if it does not exist
report_directory = Path("reports")
report_directory.mkdir(exist_ok=True)

# Define output report filename
report_file = report_directory / "sensor_analysis_report.txt"

# Prepare report content
report_lines = [
    "INDUSTRIAL SENSOR ANALYSIS REPORT",
    "=================================",
    f"Generated: {datetime.now()}",
    "",
    f"Total Measurements: {len(validated_data)}",
    f"Normal Measurements: {len(validated_data) - len(fault_records)}",
    f"Abnormal Measurements: {len(fault_records)}",
    "",
    "SENSOR STATISTICS",
    "-----------------"
]

# Add statistics for each sensor
for sensor_name, unit in sensors:

    values = [
        measurement[sensor_name]
        for measurement in validated_data
    ]

    report_lines.extend([
        "",
        sensor_name,
        f"Minimum: {min(values):.2f} {unit}",
        f"Maximum: {max(values):.2f} {unit}",
        f"Average: {sum(values) / len(values):.2f} {unit}"
    ])

# Add detected faults
report_lines.extend([
    "",
    "DETECTED FAULTS",
    "---------------"
])

if fault_records:
    for record in fault_records:
        report_lines.append(
            f"\nMeasurement {record['measurement_number']}"
        )
        report_lines.append(
            f"Timestamp: {record['timestamp']}"
        )

        for fault in record["faults"]:
            report_lines.append(f"WARNING: {fault}")
else:
    report_lines.append("No abnormal conditions detected.")

# Save the report
with open(report_file, mode="w", encoding="utf-8") as file:
    file.write("\n".join(report_lines) + "\n")

print("Engineering report generated successfully!")
print("Report saved to:", report_file)



