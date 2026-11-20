
import math
from datetime import datetime


def validate_measurement(measurement, number):

    # Convert timestamp and sensor values
    try:
        timestamp = datetime.fromisoformat(
            measurement["timestamp"]
        )

        temperature = float(measurement["temperature_C"])
        voltage = float(measurement["voltage_V"])
        current = float(measurement["current_A"])

    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(
            f"Invalid measurement {number}: {error}"
        ) from error

    # Check for NaN and infinity
    values = [temperature, voltage, current]

    if not all(math.isfinite(value) for value in values):
        raise ValueError(
            f"Non-finite value in measurement {number}"
        )

    # Return the validated measurement
    return {
        "timestamp": timestamp,
        "temperature_C": temperature,
        "voltage_V": voltage,
        "current_A": current
    }
