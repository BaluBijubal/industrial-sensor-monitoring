
# First automated test using pytest

def test_overheating_threshold_example():

    # Simulated sensor measurement
    temperature = 90

    # Defined overheating threshold
    threshold = 75

    # Verify that the measurement exceeds the threshold
    assert temperature > threshold
