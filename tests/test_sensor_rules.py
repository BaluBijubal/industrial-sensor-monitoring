
from src.sensor_rules import detect_faults


# Test 1: Normal operating conditions
def test_normal_operation():
    faults = detect_faults(50, 230, 5)
    assert faults == []


# Test 2: Motor overheating
def test_overheating():
    faults = detect_faults(90, 230, 5)
    assert faults == ["OVERHEATING: 90.00 °C"]


# Test 3: Supply undervoltage
def test_undervoltage():
    faults = detect_faults(50, 195, 5)
    assert faults == ["UNDERVOLTAGE: 195.00 V"]


# Test 4: Supply overvoltage
def test_overvoltage():
    faults = detect_faults(50, 260, 5)
    assert faults == ["OVERVOLTAGE: 260.00 V"]


# Test 5: Motor overcurrent
def test_overcurrent():
    faults = detect_faults(50, 230, 9)
    assert faults == ["OVERCURRENT: 9.00 A"]


# Test 6: Values exactly at alarm thresholds
def test_threshold_boundaries():
    faults = detect_faults(75, 207, 8)
    assert faults == []

    faults = detect_faults(50, 253, 5)
    assert faults == []


# Test 7: Multiple simultaneous faults
def test_multiple_faults():
    faults = detect_faults(90, 195, 9)

    assert faults == [
        "OVERHEATING: 90.00 °C",
        "UNDERVOLTAGE: 195.00 V",
        "OVERCURRENT: 9.00 A"
    ]
