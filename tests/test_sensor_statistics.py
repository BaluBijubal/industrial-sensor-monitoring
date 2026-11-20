
import pytest

from src.sensor_statistics import calculate_statistics


# Test 1: Normal sensor measurements
def test_normal_statistics():

    values = [40, 50, 60]

    result = calculate_statistics(values)

    assert result["minimum"] == 40
    assert result["maximum"] == 60
    assert result["average"] == 50


# Test 2: Decimal sensor measurements
def test_decimal_statistics():

    values = [4.2, 5.1, 5.8]

    result = calculate_statistics(values)

    assert result["minimum"] == 4.2
    assert result["maximum"] == 5.8
    assert result["average"] == pytest.approx(5.0333333333)


# Test 3: Single measurement
def test_single_measurement():

    values = [45]

    result = calculate_statistics(values)

    assert result["minimum"] == 45
    assert result["maximum"] == 45
    assert result["average"] == 45


# Test 4: Empty sensor dataset
def test_empty_dataset():

    with pytest.raises(ValueError):
        calculate_statistics([])
