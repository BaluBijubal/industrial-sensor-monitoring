
# Industrial sensor fault detection rules

def detect_faults(temperature, voltage, current):

    faults = []

    # Check temperature
    if temperature > 75:
        faults.append(
            f"OVERHEATING: {temperature:.2f} °C"
        )

    # Check voltage
    if voltage < 207:
        faults.append(
            f"UNDERVOLTAGE: {voltage:.2f} V"
        )

    elif voltage > 253:
        faults.append(
            f"OVERVOLTAGE: {voltage:.2f} V"
        )

    # Check current
    if current > 8:
        faults.append(
            f"OVERCURRENT: {current:.2f} A"
        )

    return faults
