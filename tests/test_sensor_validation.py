
import pytest
from datetime import datetime

from src.sensor_validation import validate_measurement


# Test 1: Valid sensor measurement
def test_valid_measurement():

    measurement = {
        "timestamp": "2026-11-17T19:39:27",
        "temperature_C": "50.46",
        "voltage_V": "230.24",
        "current_A": "5.13"
    }

    result = validate_measurement(measurement, 1)

    assert result["temperature_C"] == 50.46
    assert result["voltage_V"] == 230.24
    assert result["current_A"] == 5.13
    assert isinstance(result["timestamp"], datetime)


# Test 2: Abnormal but valid measurement
def test_abnormal_measurement_is_valid():

    measurement = {
        "timestamp": "2026-11-17T19:39:32",
        "temperature_C": "91.80",
        "voltage_V": "230.00",
        "current_A": "5.00"
    }

    result = validate_measurement(measurement, 2)

    assert result["temperature_C"] == 91.80


# Test 3: Invalid temperature
def test_invalid_temperature():

    measurement = {
        "timestamp": "2026-11-17T19:39:27",
        "temperature_C": "ERROR",
        "voltage_V": "230",
        "current_A": "5"
    }

    with pytest.raises(ValueError):
        validate_measurement(measurement, 3)


# Test 4: Missing voltage measurement
def test_missing_voltage():

    measurement = {
        "timestamp": "2026-11-17T19:39:27",
        "temperature_C": "50",
        "current_A": "5"
    }

    with pytest.raises(ValueError):
        validate_measurement(measurement, 4)


# Test 5: Invalid timestamp
def test_invalid_timestamp():

    measurement = {
        "timestamp": "INVALID_DATE",
        "temperature_C": "50",
        "voltage_V": "230",
        "current_A": "5"
    }

    with pytest.raises(ValueError):
        validate_measurement(measurement, 5)


# Test 6: Non-finite sensor measurement
def test_nan_measurement():

    measurement = {
        "timestamp": "2026-11-17T19:39:27",
        "temperature_C": "NaN",
        "voltage_V": "230",
        "current_A": "5"
    }

    with pytest.raises(ValueError):
        validate_measurement(measurement, 6)
